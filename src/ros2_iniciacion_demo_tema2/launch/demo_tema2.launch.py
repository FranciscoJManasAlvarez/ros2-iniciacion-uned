from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(package="ros2_iniciacion_demo_tema2", executable="nodo_sensor_temperatura", output="screen"),
            Node(package="ros2_iniciacion_demo_tema2", executable="nodo_estacion_acoplamiento", output="screen"),
        ]
    )
