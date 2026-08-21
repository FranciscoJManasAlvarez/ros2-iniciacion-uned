import time

from ros2_iniciacion_verificacion.tema4.gz_utils import entity_pose
from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, require_command, run_verifier

EXPECTED_POSE = (0.0, 0.0, 0.1)
TOLERANCE = 0.2


def check(node):
    require_command("gz")
    time.sleep(5.0)  # dar tiempo a que Gazebo cargue el mundo y el spawn se complete
    x, y, z = entity_pose("robot_delivery")
    got = (x, y, z)
    if any(abs(a - b) > TOLERANCE for a, b in zip(got, EXPECTED_POSE)):
        raise VerifierFailure(f"robot_delivery debería aparecer en {EXPECTED_POSE}, está en {got}")


def main():
    run_verifier("verificador_tema4_ej7", 7, check)


if __name__ == "__main__":
    main()
