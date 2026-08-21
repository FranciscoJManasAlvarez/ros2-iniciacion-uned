import yaml
from tf2_ros import Buffer, TransformListener

from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, run_verifier, spin_until

EXPECTED_FRAMES = {"base_link", "left_wheel_link", "right_wheel_link", "caster_link"}


def check(node):
    buffer = Buffer()
    TransformListener(buffer, node)

    def has_frames():
        return len(buffer.all_frames_as_yaml()) > 5

    if not spin_until(node, has_frames, timeout=15.0):
        raise VerifierFailure(
            "no se ha podido leer un árbol TF a partir de launch/ver_robot.launch.py "
            "(¿arrancan robot_state_publisher y joint_state_publisher correctamente?)"
        )

    frames = yaml.safe_load(buffer.all_frames_as_yaml()) or {}
    missing = EXPECTED_FRAMES - set(frames.keys())
    if missing:
        raise VerifierFailure(f"faltan frames en el árbol TF: {missing}")

    orphans = [
        name
        for name, info in frames.items()
        if info.get("parent") and info["parent"] not in frames and info["parent"] != "base_link"
    ]
    if orphans:
        raise VerifierFailure(f"frames con parent inexistente en el árbol TF: {orphans}")


def main():
    run_verifier("verificador_tema4_ej5", 5, check)


if __name__ == "__main__":
    main()
