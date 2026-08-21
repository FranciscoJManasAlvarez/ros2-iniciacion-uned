"""Doble de pruebas de nodo_tf_dinamico (Ej.4), usado en Ej.5 para aislar a
nodo_tf_listener (bajo prueba) de una implementación del alumno que podría
todavía no funcionar. Publica exactamente la transformación circular exigida
por el enunciado: base_link -> rotating_link, radio 0.5 m, 10 Hz.
"""
import math

import rclpy
from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from tf2_ros import TransformBroadcaster

RADIUS = 0.5
RATE_HZ = 10.0


class MockTfDinamico(Node):
    def __init__(self):
        super().__init__("mock_tf_dinamico")
        self._broadcaster = TransformBroadcaster(self)
        self._t0 = self.get_clock().now()
        self.create_timer(1.0 / RATE_HZ, self._tick)

    def _tick(self):
        elapsed = (self.get_clock().now() - self._t0).nanoseconds / 1e9
        angle = elapsed
        tf = TransformStamped()
        tf.header.stamp = self.get_clock().now().to_msg()
        tf.header.frame_id = "base_link"
        tf.child_frame_id = "rotating_link"
        tf.transform.translation.x = RADIUS * math.cos(angle)
        tf.transform.translation.y = RADIUS * math.sin(angle)
        tf.transform.translation.z = 0.0
        tf.transform.rotation.w = 1.0
        self._broadcaster.sendTransform(tf)


def main():
    rclpy.init()
    node = MockTfDinamico()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
