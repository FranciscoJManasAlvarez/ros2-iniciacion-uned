from ros2_iniciacion_verificacion.verifier_base import run_verifier, wait_for_node, wait_for_topic_type

NAMESPACE = "/robot1"
NODES = ["nodo_datos_demo", "nodo_goal_listener", "nodo_servicio_demo", "nodo_gui_pyqt"]


def check(node):
    for name in NODES:
        wait_for_node(node, name, namespace=NAMESPACE)
    wait_for_topic_type(node, f"{NAMESPACE}/scan", "sensor_msgs/msg/LaserScan")
    wait_for_topic_type(node, f"{NAMESPACE}/odom", "nav_msgs/msg/Odometry")


def main():
    run_verifier("verificador_tema5_ej9", 9, check)


if __name__ == "__main__":
    main()
