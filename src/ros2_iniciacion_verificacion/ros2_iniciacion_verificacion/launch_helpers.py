"""Helpers compartidos por los 36 ficheros launch/temaXejercicioN.launch.py.

Cada ejercicio se resuelve con el mismo patrón: arrancar el/los nodo(s) exigidos
al alumno (por su nombre exacto de paquete/ejecutable) junto con un nodo
verificador; cuando el verificador termina (éxito o fallo), toda la red ROS 2
se apaga automáticamente.
"""
from launch import LaunchDescription
from launch.actions import EmitEvent, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.events import Shutdown
from launch_ros.actions import Node


def student_node(package, executable, **kwargs):
    kwargs.setdefault("output", "screen")
    return Node(package=package, executable=executable, **kwargs)


def verifier_launch(
    verifier_executable,
    extra_actions=None,
    verifier_args=None,
    verifier_parameters=None,
    launch_arguments=None,
):
    verifier = Node(
        package="ros2_iniciacion_verificacion",
        executable=verifier_executable,
        output="screen",
        arguments=verifier_args or [],
        parameters=verifier_parameters or [],
    )
    actions = list(launch_arguments or []) + list(extra_actions or []) + [verifier]
    actions.append(
        RegisterEventHandler(
            OnProcessExit(target_action=verifier, on_exit=[EmitEvent(event=Shutdown())])
        )
    )
    return LaunchDescription(actions)
