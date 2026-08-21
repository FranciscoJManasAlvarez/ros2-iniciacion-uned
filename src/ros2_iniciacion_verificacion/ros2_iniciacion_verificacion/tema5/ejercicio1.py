import rclpy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from tf2_ros import Buffer, TransformListener

from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    collect_messages,
    run_verifier,
    spin_until,
    wait_for_topic_type,
)


def check(node):
    wait_for_topic_type(node, "/robot1/scan", "sensor_msgs/msg/LaserScan")
    wait_for_topic_type(node, "/robot1/odom", "nav_msgs/msg/Odometry")
    collect_messages(node, "/robot1/scan", LaserScan, count=1, timeout=6.0)
    collect_messages(node, "/robot1/odom", Odometry, count=1, timeout=6.0)

    buffer = Buffer()
    TransformListener(buffer, node)

    def resolvable():
        return buffer.can_transform("odom", "base_link", rclpy.time.Time())

    if not spin_until(node, resolvable, timeout=8.0):
        raise VerifierFailure("no se puede resolver la transformación odom -> base_link")


def main():
    run_verifier("verificador_tema5_ej1", 1, check)


if __name__ == "__main__":
    main()
