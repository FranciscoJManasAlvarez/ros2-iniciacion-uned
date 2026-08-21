from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(package="ros2_iniciacion_demo_tema3", executable="nodo_tf_soporte_camara", output="screen"),
            Node(package="ros2_iniciacion_demo_tema3", executable="nodo_tf_brazo", output="screen"),
        ]
    )
