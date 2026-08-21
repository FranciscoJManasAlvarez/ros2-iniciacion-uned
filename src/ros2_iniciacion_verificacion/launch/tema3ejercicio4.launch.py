from ros2_iniciacion_verificacion.launch_helpers import student_node, verifier_launch


def generate_launch_description():
    return verifier_launch(
        "verificador_tema3_ej4",
        extra_actions=[student_node("tema3_practica", "nodo_tf_dinamico")],
    )
