from std_msgs.msg import Float32

from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    collect_messages,
    rosout_messages,
    run_verifier,
    wait_for_node,
)

INFO = 20


def check(node):
    wait_for_node(node, "mock_navegacion")
    wait_for_node(node, "nodo_hola")

    msgs = collect_messages(node, "/mock/navegacion_goal_distancia", Float32, count=1, timeout=10.0)
    if abs(msgs[0].data - 5.0) > 1e-3:
        raise VerifierFailure(f"nodo_hola debería enviar distancia_objetivo=5.0, ha enviado {msgs[0].data}")

    entries = rosout_messages(node, "nodo_hola", timeout=6.0, min_level=INFO)
    if len(entries) < 5:
        raise VerifierFailure(
            "nodo_hola debería registrar (INFO) el feedback recibido y el resultado final "
            f"(se han observado {len(entries)} mensajes INFO tras el goal)"
        )


def main():
    run_verifier("verificador_tema2_ej8", 8, check)


if __name__ == "__main__":
    main()
