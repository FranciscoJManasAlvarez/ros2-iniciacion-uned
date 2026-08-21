import time

from ros2_iniciacion_verificacion.tema4.gz_utils import entity_pose
from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, require_command, run_verifier


def check(node):
    require_command("gz")
    time.sleep(5.0)
    x0, _, _ = entity_pose("robot_delivery")
    time.sleep(4.0)  # a 0.2 m/s deberían recorrerse ~0.8 m en este intervalo
    x1, _, _ = entity_pose("robot_delivery")

    if (x1 - x0) < 0.2:
        raise VerifierFailure(
            f"la posición x de robot_delivery no avanza de forma sostenida (x0={x0}, x1={x1}); "
            "revisa nodo_teleop_gazebo y su integración en sim_gazebo.launch.py"
        )


def main():
    run_verifier("verificador_tema4_ej9", 9, check)


if __name__ == "__main__":
    main()
