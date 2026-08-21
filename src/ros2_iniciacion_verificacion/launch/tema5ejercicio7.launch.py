from launch.actions import SetEnvironmentVariable

from ros2_iniciacion_verificacion.launch_helpers import student_node, verifier_launch


def generate_launch_description():
    return verifier_launch(
        "verificador_tema5_ej7",
        extra_actions=[
            SetEnvironmentVariable("QT_QPA_PLATFORM", "offscreen"),
            student_node("tema5_practica", "nodo_gui_pyqt"),
        ],
    )
