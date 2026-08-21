from std_msgs.msg import Float32

from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    collect_messages,
    run_verifier,
    wait_for_node,
    wait_for_topic_type,
)

EXPECTED_RADIUS = 0.5
TOLERANCE = 0.15


def check(node):
    wait_for_node(node, "mock_tf_dinamico")
    wait_for_node(node, "nodo_tf_listener")
    wait_for_topic_type(node, "/robot1/distancia_tf", "std_msgs/msg/Float32")

    msgs = collect_messages(node, "/robot1/distancia_tf", Float32, count=3, timeout=8.0)
    for m in msgs:
        if abs(m.data - EXPECTED_RADIUS) > TOLERANCE:
            raise VerifierFailure(
                f"/robot1/distancia_tf debería rondar {EXPECTED_RADIUS} m, se ha recibido {m.data}"
            )


def main():
    run_verifier("verificador_tema3_ej5", 5, check)


if __name__ == "__main__":
    main()
