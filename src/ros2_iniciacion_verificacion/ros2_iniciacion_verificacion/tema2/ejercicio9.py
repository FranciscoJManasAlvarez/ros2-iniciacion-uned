from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    get_remote_param,
    run_verifier,
    wait_for_node,
    wait_for_topic_type,
)

NAMESPACE = "/robot1"
NODES = [
    "nodo_sensor",
    "nodo_monitor",
    "nodo_estado",
    "nodo_estacion_carga",
    "nodo_navegacion",
    "nodo_hola",
]


def check(node):
    for name in NODES:
        wait_for_node(node, name, namespace=NAMESPACE)

    wait_for_topic_type(node, f"{NAMESPACE}/robot/bateria", "std_msgs/msg/Float32")

    # Se lanza con un valor distinto del por defecto (ver launch/tema2ejercicio9.launch.py)
    # precisamente para que esta comprobación no pase "por casualidad".
    expected = 33.0
    value = get_remote_param(node, f"{NAMESPACE}/nodo_monitor", "umbral_bateria")
    if abs(value.double_value - expected) > 1e-6:
        raise VerifierFailure(
            "el argumento de lanzamiento 'umbral_bateria' no se ha propagado a nodo_monitor "
            f"(esperado {expected}, obtenido {value.double_value})"
        )


def main():
    run_verifier("verificador_tema2_ej9", 9, check)


if __name__ == "__main__":
    main()
