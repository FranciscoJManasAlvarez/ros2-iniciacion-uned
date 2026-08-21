from ros2_iniciacion_verificacion.tema4.urdf_utils import find_link, find_share_file, parse_urdf_file
from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, run_verifier

EXPECTED_MASS = 5.0


def check(node):
    path = find_share_file("tema4_practica", "urdf/robot_delivery.urdf")
    root = parse_urdf_file(path)

    base_link = find_link(root, "base_link")
    if base_link is None:
        raise VerifierFailure("no existe el link 'base_link' en robot_delivery.urdf")

    for tag in ("visual", "collision", "inertial"):
        if base_link.find(tag) is None:
            raise VerifierFailure(f"'base_link' no tiene el bloque <{tag}>")

    mass_el = base_link.find("inertial/mass")
    if mass_el is None or abs(float(mass_el.get("value", "0")) - EXPECTED_MASS) > 1e-6:
        raise VerifierFailure(f"la masa de 'base_link' debería ser {EXPECTED_MASS} kg")


def main():
    run_verifier("verificador_tema4_ej1", 1, check)


if __name__ == "__main__":
    main()
