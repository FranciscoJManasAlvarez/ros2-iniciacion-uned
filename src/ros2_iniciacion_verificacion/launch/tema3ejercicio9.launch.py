from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

from ros2_iniciacion_verificacion.launch_helpers import verifier_launch


def generate_launch_description():
    student_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [FindPackageShare("tema3_practica"), "launch", "practica_tema3.launch.py"]
            )
        )
    )
    return verifier_launch(
        "verificador_tema3_ej9",
        launch_arguments=[DeclareLaunchArgument("student_repo_path", default_value=".")],
        extra_actions=[student_launch],
        verifier_parameters=[{"student_repo_path": LaunchConfiguration("student_repo_path")}],
    )
