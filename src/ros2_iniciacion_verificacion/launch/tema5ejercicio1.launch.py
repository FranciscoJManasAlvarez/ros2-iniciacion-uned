from ros2_iniciacion_verificacion.launch_helpers import student_node, verifier_launch


def generate_launch_description():
    return verifier_launch(
        "verificador_tema5_ej1",
        extra_actions=[student_node("tema5_practica", "nodo_datos_demo")],
    )
