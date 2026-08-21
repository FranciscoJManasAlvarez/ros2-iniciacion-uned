import rclpy
from tf2_ros import Buffer, TransformListener

from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, run_verifier, spin_until


def check(node):
    buffer = Buffer()
    TransformListener(buffer, node)

    def resolvable():
        return buffer.can_transform("base_link", "sensor_frame", rclpy.time.Time())

    if not spin_until(node, resolvable, timeout=10.0):
        raise VerifierFailure("no se puede resolver la transformación base_link -> sensor_frame")

    t1 = buffer.lookup_transform("base_link", "sensor_frame", rclpy.time.Time())
    import time

    time.sleep(1.0)
    for _ in range(10):
        rclpy.spin_once(node, timeout_sec=0.1)
    t2 = buffer.lookup_transform("base_link", "sensor_frame", rclpy.time.Time())

    d = (
        (t1.transform.translation.x - t2.transform.translation.x) ** 2
        + (t1.transform.translation.y - t2.transform.translation.y) ** 2
        + (t1.transform.translation.z - t2.transform.translation.z) ** 2
    ) ** 0.5
    if d > 1e-3:
        raise VerifierFailure("base_link -> sensor_frame debería ser una transformación estática (constante)")


def main():
    run_verifier("verificador_tema3_ej3", 3, check)


if __name__ == "__main__":
    main()
