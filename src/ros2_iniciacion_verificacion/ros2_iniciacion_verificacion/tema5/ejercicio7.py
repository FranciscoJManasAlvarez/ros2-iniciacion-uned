import time

from std_msgs.msg import Float32

from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, run_verifier, spin_until, wait_for_node


def check(node):
    wait_for_node(node, "nodo_gui_pyqt")
    pub = node.create_publisher(Float32, "/robot/bateria", 10)
    time.sleep(0.5)
    pub.publish(Float32(data=42.0))

    def subscribed():
        subs = node.get_subscriptions_info_by_topic("/robot/bateria")
        return any(s.node_name == "nodo_gui_pyqt" for s in subs)

    if not spin_until(node, subscribed, timeout=8.0):
        raise VerifierFailure("nodo_gui_pyqt no aparece como suscriptor de /robot/bateria")


def main():
    run_verifier("verificador_tema5_ej7", 7, check)


if __name__ == "__main__":
    main()
