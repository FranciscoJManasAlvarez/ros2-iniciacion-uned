from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

from ros2_iniciacion_verificacion.launch_helpers import verifier_launch


def generate_launch_description():
    student_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare("tema5_practica"), "launch", "foxglove.launch.py"])
        )
    )
    return verifier_launch("verificador_tema5_ej5", extra_actions=[student_launch])
