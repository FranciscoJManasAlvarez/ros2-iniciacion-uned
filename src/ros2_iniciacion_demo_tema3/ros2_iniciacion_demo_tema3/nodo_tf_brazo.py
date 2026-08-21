"""Demo de TF dinámica: articulación de un brazo pinza de RobotDelivery, con
nombres de frame distintos a los del Ej.4 evaluado (base_link -> rotating_link)."""
import math

import rclpy
from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from tf2_ros import TransformBroadcaster

AMPLITUDE_RAD = 0.5


class NodoTfBrazo(Node):
    def __init__(self):
        super().__init__("nodo_tf_brazo")
        self._broadcaster = TransformBroadcaster(self)
        self._t0 = self.get_clock().now()
        self.create_timer(0.1, self._tick)

    def _tick(self):
        elapsed = (self.get_clock().now() - self._t0).nanoseconds / 1e9
        angle = AMPLITUDE_RAD * math.sin(elapsed)
        tf = TransformStamped()
        tf.header.stamp = self.get_clock().now().to_msg()
        tf.header.frame_id = "base_link"
        tf.child_frame_id = "gripper_joint_frame"
        tf.transform.rotation.z = math.sin(angle / 2.0)
        tf.transform.rotation.w = math.cos(angle / 2.0)
        self._broadcaster.sendTransform(tf)


def main():
    rclpy.init()
    try:
        rclpy.spin(NodoTfBrazo())
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()
