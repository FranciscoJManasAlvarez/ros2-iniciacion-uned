from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    xacro_path = PathJoinSubstitution(
        [FindPackageShare("ros2_iniciacion_demo_tema4"), "urdf", "mastil_sensores.urdf.xacro"]
    )
    robot_description = Command(["xacro ", xacro_path])

    return LaunchDescription(
        [
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                output="screen",
                parameters=[{"robot_description": robot_description}],
            ),
            Node(package="joint_state_publisher", executable="joint_state_publisher", output="screen"),
            Node(package="rviz2", executable="rviz2", output="screen"),
        ]
    )
