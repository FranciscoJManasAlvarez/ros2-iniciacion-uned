from tf2_msgs.msg import TFMessage

from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, collect_messages, run_verifier, wait_for_node


def check(node):
    wait_for_node(node, "nodo_bag_checker")
    try:
        collect_messages(node, "/tf", TFMessage, count=1, timeout=10.0)
    except VerifierFailure:
        raise VerifierFailure(
            "no se ha recibido ningún mensaje /tf durante la reproducción del bag "
            "(¿se ha lanzado 'ros2 bag play' sobre bags/tema3_bag?)"
        )


def main():
    run_verifier("verificador_tema3_ej7", 7, check)


if __name__ == "__main__":
    main()
