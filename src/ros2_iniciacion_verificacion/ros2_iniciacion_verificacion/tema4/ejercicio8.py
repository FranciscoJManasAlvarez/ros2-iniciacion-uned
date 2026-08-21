from sensor_msgs.msg import LaserScan

from ros2_iniciacion_verificacion.verifier_base import (
    collect_messages,
    require_command,
    run_verifier,
    wait_for_topic_type,
)


def check(node):
    require_command("gz")
    wait_for_topic_type(node, "/robot1/scan", "sensor_msgs/msg/LaserScan", timeout=25.0)
    collect_messages(node, "/robot1/scan", LaserScan, count=1, timeout=15.0)


def main():
    run_verifier("verificador_tema4_ej8", 8, check)


if __name__ == "__main__":
    main()
