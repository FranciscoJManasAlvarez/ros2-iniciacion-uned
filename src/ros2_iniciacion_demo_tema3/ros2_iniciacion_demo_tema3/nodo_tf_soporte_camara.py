"""Demo de TF estática: soporte de cámara de RobotDelivery, con nombres de
frame distintos a los del Ej.3 evaluado (base_link -> sensor_frame)."""
import rclpy
from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from tf2_ros import StaticTransformBroadcaster


class NodoTfSoporteCamara(Node):
    def __init__(self):
        super().__init__("nodo_tf_soporte_camara")
        broadcaster = StaticTransformBroadcaster(self)
        tf = TransformStamped()
        tf.header.stamp = self.get_clock().now().to_msg()
        tf.header.frame_id = "base_link"
        tf.child_frame_id = "camera_mount_frame"
        tf.transform.translation.x = 0.2
        tf.transform.translation.z = 0.25
        tf.transform.rotation.w = 1.0
        broadcaster.sendTransform(tf)


def main():
    rclpy.init()
    try:
        rclpy.spin(NodoTfSoporteCamara())
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()
