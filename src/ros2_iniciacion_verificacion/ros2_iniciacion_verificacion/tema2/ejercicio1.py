from ros2_iniciacion_verificacion.verifier_base import run_verifier, wait_for_node


def check(node):
    wait_for_node(node, "nodo_hola")


def main():
    run_verifier("verificador_tema2_ej1", 1, check)


if __name__ == "__main__":
    main()
