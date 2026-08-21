from ros2_iniciacion_verificacion.launch_helpers import student_node, verifier_launch


def generate_launch_description():
    return verifier_launch(
        "verificador_tema2_ej7",
        extra_actions=[
            student_node("tema2_practica", "nodo_navegacion"),
            student_node("ros2_iniciacion_verificacion", "mock_estacion_carga"),
        ],
    )
