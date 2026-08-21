from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

from ros2_iniciacion_verificacion.launch_helpers import verifier_launch


def generate_launch_description():
    offscreen = SetEnvironmentVariable("QT_QPA_PLATFORM", "offscreen")
    student_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([FindPackageShare("tema4_practica"), "launch", "ver_robot.launch.py"])
        )
    )
    return verifier_launch("verificador_tema4_ej5", extra_actions=[offscreen, student_launch])
