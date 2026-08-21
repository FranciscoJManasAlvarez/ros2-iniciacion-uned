from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, run_verifier, wait_for_node, wait_for_topic_type


def check(node):
    # NOTA: el enunciado prevé simular la pulsación del botón con QTest, lo que
    # exige un punto de entrada de clase conocido (p.ej. `tema5_practica.nodo_gui_pyqt:MainWindow`)
    # que el enunciado no especifica. En su ausencia, esta comprobación se
    # limita a la interfaz pública observable: que el nodo existe y que
    # publica /robot1/comando con el tipo correcto. Ver README (Notas).
    wait_for_node(node, "nodo_gui_pyqt")
    wait_for_topic_type(node, "/robot1/comando", "std_msgs/msg/String")

    publishers = node.get_publishers_info_by_topic("/robot1/comando")
    if not any(p.node_name == "nodo_gui_pyqt" for p in publishers):
        raise VerifierFailure("nodo_gui_pyqt no aparece como publicador de /robot1/comando")


def main():
    run_verifier("verificador_tema5_ej6", 6, check)


if __name__ == "__main__":
    main()
