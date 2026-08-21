from ros2_iniciacion_verificacion.launch_helpers import student_node, verifier_launch


def generate_launch_description():
    return verifier_launch(
        "verificador_tema5_ej8",
        extra_actions=[student_node("tema5_practica", "nodo_servicio_demo")],
    )
