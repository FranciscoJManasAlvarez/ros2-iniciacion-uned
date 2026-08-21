from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, require_ros_package, run_verifier, tcp_port_open

FOXGLOVE_PORT = 8765


def check(node):
    require_ros_package("foxglove_bridge")
    if not tcp_port_open("localhost", FOXGLOVE_PORT, timeout=20.0):
        raise VerifierFailure(
            f"el puerto WebSocket de foxglove_bridge ({FOXGLOVE_PORT}) no acepta conexiones"
        )


def main():
    run_verifier("verificador_tema5_ej5", 5, check)


if __name__ == "__main__":
    main()
