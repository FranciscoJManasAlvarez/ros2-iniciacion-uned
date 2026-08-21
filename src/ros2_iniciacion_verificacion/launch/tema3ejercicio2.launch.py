from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from ros2_iniciacion_verificacion.launch_helpers import verifier_launch


def generate_launch_description():
    return verifier_launch(
        "verificador_tema3_ej2",
        launch_arguments=[DeclareLaunchArgument("student_repo_path", default_value=".")],
        verifier_parameters=[{"student_repo_path": LaunchConfiguration("student_repo_path")}],
    )
