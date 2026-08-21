import time

from std_msgs.msg import Float32, Int32

from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    collect_messages,
    run_verifier,
    wait_for_node,
)


def check(node):
    wait_for_node(node, "mock_estacion_carga")
    wait_for_node(node, "nodo_monitor")

    pub = node.create_publisher(Float32, "/robot/bateria", 10)
    time.sleep(0.5)
    pub.publish(Float32(data=5.0))

    try:
        collect_messages(node, "/mock/solicitar_carga_calls", Int32, count=1, timeout=6.0)
    except VerifierFailure:
        raise VerifierFailure(
            "nodo_monitor no ha llamado a /robot/solicitar_carga al recibir una batería baja"
        )


def main():
    run_verifier("verificador_tema2_ej6", 6, check)


if __name__ == "__main__":
    main()
