import math
import time

import rclpy
from tf2_ros import Buffer, TransformListener

from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, run_verifier, spin_until

EXPECTED_RADIUS = 0.5
TOLERANCE = 0.1


def check(node):
    buffer = Buffer()
    TransformListener(buffer, node)

    def resolvable():
        return buffer.can_transform("base_link", "rotating_link", rclpy.time.Time())

    if not spin_until(node, resolvable, timeout=10.0):
        raise VerifierFailure("no se puede resolver la transformación base_link -> rotating_link")

    samples = []
    for _ in range(8):
        t = buffer.lookup_transform("base_link", "rotating_link", rclpy.time.Time())
        samples.append((t.transform.translation.x, t.transform.translation.y))
        time.sleep(0.15)
        for _ in range(3):
            rclpy.spin_once(node, timeout_sec=0.05)

    radii = [math.hypot(x, y) for x, y in samples]
    if any(abs(r - EXPECTED_RADIUS) > TOLERANCE for r in radii):
        raise VerifierFailure(
            f"el radio de la trayectoria circular debería ser ~{EXPECTED_RADIUS} m, se han observado {radii}"
        )
    if len({round(x, 3) for x, _ in samples}) < 2:
        raise VerifierFailure("rotating_link no parece moverse (posición x constante en el tiempo)")


def main():
    run_verifier("verificador_tema3_ej4", 4, check)


if __name__ == "__main__":
    main()
