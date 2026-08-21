"""Utilidades comunes para los nodos verificadores de todos los temas.

Cada ejercicio se valida con un único proceso ROS 2 de vida corta: hace sus
comprobaciones, imprime el veredicto con el formato exigido por los enunciados
y termina. `run_verifier` centraliza ese ciclo de vida para que cada módulo
`temaN/ejercicioM.py` solo tenga que implementar la función `check(node)`.
"""
import sys
import time
import socket

import rclpy
from rclpy.node import Node

DEFAULT_TIMEOUT = 12.0


class VerifierFailure(Exception):
    """Señala que la comprobación ha fallado; el mensaje se usa como diagnóstico."""


def run_verifier(node_name, exercise_num, check_fn):
    """Crea un nodo `node_name`, ejecuta `check_fn(node)` y termina el proceso.

    `check_fn` debe devolver normalmente si el ejercicio se supera, o lanzar
    `VerifierFailure(motivo)` si no. El código de salida (0/1) es lo que las
    plantillas de lanzamiento usan para decidir si mostrar éxito o fallo.
    """
    rclpy.init()
    node = Node(node_name)
    try:
        check_fn(node)
        node.get_logger().info(
            f"[verificador]: OK - Ejercicio {exercise_num} superado correctamente"
        )
        sys.exit(0)
    except VerifierFailure as exc:
        node.get_logger().error(f"[verificador]: FAIL - {exc}")
        sys.exit(1)
    except Exception as exc:  # noqa: BLE001 - un fallo inesperado también es un FAIL
        node.get_logger().error(f"[verificador]: FAIL - error inesperado: {exc}")
        sys.exit(1)
    finally:
        node.destroy_node()
        rclpy.shutdown()


def spin_until(node, predicate, timeout=DEFAULT_TIMEOUT, period=0.05):
    """Hace spin de `node` hasta que `predicate()` sea verdad o venza el timeout."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        rclpy.spin_once(node, timeout_sec=period)
        if predicate():
            return True
    return False


def wait_for_node(node, target_name, namespace="/", timeout=DEFAULT_TIMEOUT):
    """Comprueba que `target_name` aparece en `ros2 node list` (con namespace opcional)."""

    def present():
        names = node.get_node_names_and_namespaces()
        for name, ns in names:
            if name == target_name and (namespace in ("/", "", None) or ns == namespace):
                return True
        return False

    if not spin_until(node, present, timeout):
        raise VerifierFailure(
            f"el nodo '{target_name}' (namespace '{namespace}') no ha aparecido en el grafo ROS 2"
        )


def wait_for_topic_type(node, topic, expected_type, timeout=DEFAULT_TIMEOUT):
    """Comprueba que `topic` existe y se publica/suscribe con el tipo `expected_type`."""

    def present():
        for name, types in node.get_topic_names_and_types():
            if name == topic and expected_type in types:
                return True
        return False

    if not spin_until(node, present, timeout):
        raise VerifierFailure(
            f"el topic '{topic}' no existe con el tipo '{expected_type}' tras {timeout}s"
        )


def collect_messages(node, topic, msg_type, count, timeout=DEFAULT_TIMEOUT):
    """Se suscribe a `topic` y devuelve hasta `count` mensajes recibidos en `timeout`s."""
    received = []
    sub = node.create_subscription(msg_type, topic, lambda msg: received.append(msg), 10)
    try:
        spin_until(node, lambda: len(received) >= count, timeout)
    finally:
        node.destroy_subscription(sub)
    if not received:
        raise VerifierFailure(f"no se ha recibido ningún mensaje en '{topic}' tras {timeout}s")
    return received


def call_service(node, srv_name, srv_type, request, timeout=DEFAULT_TIMEOUT):
    """Llama a `srv_name` y devuelve la respuesta, o lanza VerifierFailure."""
    client = node.create_client(srv_type, srv_name)
    try:
        if not client.wait_for_service(timeout_sec=timeout):
            raise VerifierFailure(f"el servicio '{srv_name}' no está disponible tras {timeout}s")
        future = client.call_async(request)
        if not spin_until(node, future.done, timeout):
            raise VerifierFailure(f"la llamada a '{srv_name}' no ha respondido tras {timeout}s")
        if future.exception() is not None:
            raise VerifierFailure(f"la llamada a '{srv_name}' lanzó una excepción: {future.exception()}")
        return future.result()
    finally:
        node.destroy_client(client)


def set_remote_param(node, target_node, param_name, value, value_type, timeout=DEFAULT_TIMEOUT):
    """Equivalente a `ros2 param set /target_node param_name value`."""
    from rcl_interfaces.srv import SetParameters
    from rcl_interfaces.msg import Parameter, ParameterValue

    pv = ParameterValue(type=value_type)
    if value_type == 3:  # PARAMETER_DOUBLE
        pv.double_value = float(value)
    elif value_type == 2:  # PARAMETER_INTEGER
        pv.integer_value = int(value)
    elif value_type == 4:  # PARAMETER_STRING
        pv.string_value = str(value)
    elif value_type == 1:  # PARAMETER_BOOL
        pv.bool_value = bool(value)
    else:
        raise VerifierFailure(f"tipo de parámetro no soportado: {value_type}")

    request = SetParameters.Request(parameters=[Parameter(name=param_name, value=pv)])
    service_name = f"{target_node}/set_parameters"
    response = call_service(node, service_name, SetParameters, request, timeout)
    if not response.results or not response.results[0].successful:
        raise VerifierFailure(f"no se pudo fijar el parámetro '{param_name}' en '{target_node}'")


def get_remote_param(node, target_node, param_name, timeout=DEFAULT_TIMEOUT):
    """Equivalente a `ros2 param get /target_node param_name`. Devuelve el ParameterValue."""
    from rcl_interfaces.srv import GetParameters

    request = GetParameters.Request(names=[param_name])
    service_name = f"{target_node}/get_parameters"
    response = call_service(node, service_name, GetParameters, request, timeout)
    if not response.values:
        raise VerifierFailure(f"el parámetro '{param_name}' no existe en '{target_node}'")
    return response.values[0]


def rosout_messages(node, node_name, timeout, min_level=None):
    """Recoge lo publicado en /rosout por `node_name` durante `timeout` segundos."""
    from rcl_interfaces.msg import Log

    entries = []

    def on_log(msg):
        if msg.name == node_name or msg.name.endswith(f"/{node_name}"):
            if min_level is None or msg.level >= min_level:
                entries.append(msg)

    sub = node.create_subscription(Log, "/rosout", on_log, 50)
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        rclpy.spin_once(node, timeout_sec=0.05)
    node.destroy_subscription(sub)
    return entries


def send_action_goal(node, action_name, action_type, goal_msg, timeout=DEFAULT_TIMEOUT):
    """Envía un goal, devuelve (feedback_list, result). Lanza VerifierFailure si algo falla."""
    from rclpy.action import ActionClient

    client = ActionClient(node, action_type, action_name)
    feedback_list = []
    try:
        if not client.wait_for_server(timeout_sec=timeout):
            raise VerifierFailure(f"la acción '{action_name}' no está disponible tras {timeout}s")

        send_future = client.send_goal_async(
            goal_msg, feedback_callback=lambda fb: feedback_list.append(fb.feedback)
        )
        if not spin_until(node, send_future.done, timeout):
            raise VerifierFailure(f"no se ha podido enviar el goal a '{action_name}'")
        goal_handle = send_future.result()
        if not goal_handle.accepted:
            raise VerifierFailure(f"el goal a '{action_name}' fue rechazado")

        result_future = goal_handle.get_result_async()
        if not spin_until(node, result_future.done, timeout):
            raise VerifierFailure(f"la acción '{action_name}' no ha devuelto resultado tras {timeout}s")
        return feedback_list, result_future.result().result
    finally:
        client.destroy()


def tcp_port_open(host, port, timeout=DEFAULT_TIMEOUT):
    """Comprueba que un puerto TCP acepta conexiones (p.ej. websocket de foxglove_bridge)."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection((host, port), timeout=1.0):
                return True
        except OSError:
            time.sleep(0.3)
    return False


def student_repo_path(node):
    """Ruta a la raíz del repositorio del alumno, vía el parámetro/launch arg
    `student_repo_path` (por defecto, el directorio de trabajo actual)."""
    import os

    node.declare_parameter("student_repo_path", ".")
    return os.path.abspath(node.get_parameter("student_repo_path").value)


def require_file(base_path, relative_path):
    import os

    full_path = os.path.join(base_path, relative_path)
    if not os.path.isfile(full_path):
        raise VerifierFailure(f"no se encuentra el fichero '{relative_path}' en '{base_path}'")
    return full_path


def find_package_share_file(package, relative_path):
    """Localiza `relative_path` dentro del share instalado de `package` (p.ej.
    urdf/config que el alumno debe instalar como datos de su propio paquete)."""
    import os

    from ament_index_python.packages import PackageNotFoundError, get_package_share_directory

    try:
        share_dir = get_package_share_directory(package)
    except PackageNotFoundError:
        raise VerifierFailure(
            f"el paquete '{package}' no está compilado en este workspace "
            "(¿está en src/ junto a ros2_iniciacion_verificacion y se ha hecho colcon build?)"
        )
    full_path = os.path.join(share_dir, relative_path)
    if not os.path.isfile(full_path):
        raise VerifierFailure(f"no se encuentra '{relative_path}' en el share de '{package}'")
    return full_path


def require_command(name):
    """Lanza VerifierFailure con un diagnóstico claro si `name` no está en el PATH."""
    import shutil

    if shutil.which(name) is None:
        raise VerifierFailure(
            f"'{name}' no está instalado en este entorno; no se puede completar esta comprobación"
        )


def require_ros_package(name):
    """Lanza VerifierFailure con un diagnóstico claro si el paquete ROS `name` no está instalado."""
    from ament_index_python.packages import PackageNotFoundError, get_package_prefix

    try:
        get_package_prefix(name)
    except PackageNotFoundError:
        raise VerifierFailure(
            f"el paquete ROS '{name}' no está instalado en este entorno; no se puede completar esta comprobación"
        )
