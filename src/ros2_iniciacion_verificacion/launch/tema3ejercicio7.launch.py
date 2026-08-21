from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

from ros2_iniciacion_verificacion.launch_helpers import student_node, verifier_launch


def generate_launch_description():
    student_repo_path = LaunchConfiguration("student_repo_path")
    bag_path = PathJoinSubstitution([student_repo_path, "bags", "tema3_bag"])
    bag_play = ExecuteProcess(cmd=["ros2", "bag", "play", bag_path], output="screen")

    return verifier_launch(
        "verificador_tema3_ej7",
        launch_arguments=[DeclareLaunchArgument("student_repo_path", default_value=".")],
        extra_actions=[student_node("tema3_practica", "nodo_bag_checker"), bag_play],
    )
