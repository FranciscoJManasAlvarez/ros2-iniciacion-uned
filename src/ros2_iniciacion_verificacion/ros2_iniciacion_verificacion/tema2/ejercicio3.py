from std_msgs.msg import Float32

from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    rosout_messages,
    run_verifier,
    wait_for_node,
)

WARN = 30


def check(node):
    wait_for_node(node, "nodo_monitor")
    pub = node.create_publisher(Float32, "/robot/bateria", 10)

    import time

    time.sleep(0.5)
    pub.publish(Float32(data=50.0))
    time.sleep(0.5)
    pub.publish(Float32(data=10.0))

    entries = rosout_messages(node, "nodo_monitor", timeout=5.0, min_level=WARN)
    if not entries:
        raise VerifierFailure(
            "nodo_monitor no ha registrado un mensaje de advertencia al recibir batería por "
            "debajo de 'umbral_bateria'"
        )


def main():
    run_verifier("verificador_tema2_ej3", 3, check)


if __name__ == "__main__":
    main()
