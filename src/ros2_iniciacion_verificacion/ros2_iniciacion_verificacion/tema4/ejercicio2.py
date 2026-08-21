from ros2_iniciacion_verificacion.tema4.urdf_utils import find_joint, find_link, find_share_file, parse_urdf_file
from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, run_verifier

WHEEL_LINKS = ["left_wheel_link", "right_wheel_link", "caster_link"]
JOINTS = {
    "left_wheel_joint": "continuous",
    "right_wheel_joint": "continuous",
    "caster_joint": "fixed",
}


def check(node):
    path = find_share_file("tema4_practica", "urdf/robot_delivery.urdf")
    root = parse_urdf_file(path)

    for name in WHEEL_LINKS:
        if find_link(root, name) is None:
            raise VerifierFailure(f"falta el link '{name}'")

    for name, expected_type in JOINTS.items():
        joint = find_joint(root, name)
        if joint is None:
            raise VerifierFailure(f"falta el joint '{name}'")
        if joint.get("type") != expected_type:
            raise VerifierFailure(f"'{name}' debería ser de tipo '{expected_type}', es '{joint.get('type')}'")
        parent = joint.find("parent")
        if parent is None or parent.get("link") != "base_link":
            raise VerifierFailure(f"'{name}' debería tener 'base_link' como parent")


def main():
    run_verifier("verificador_tema4_ej2", 2, check)


if __name__ == "__main__":
    main()
