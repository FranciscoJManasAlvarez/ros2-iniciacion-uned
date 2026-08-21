import xml.etree.ElementTree as ET

from ros2_iniciacion_verificacion.tema4.urdf_utils import find_share_file
from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, run_verifier

EXPECTED_GRAVITY = (0.0, 0.0, -9.8)


def check(node):
    path = find_share_file("tema4_practica", "worlds/almacen.sdf")
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        raise VerifierFailure(f"'{path}' no es un SDF/XML válido: {exc}")

    world = root.find("world")
    if world is None:
        raise VerifierFailure("almacen.sdf no contiene un elemento <world>")

    gravity_el = world.find("gravity")
    if gravity_el is None:
        raise VerifierFailure("falta <gravity> en el mundo")
    gravity = tuple(float(v) for v in gravity_el.text.split())
    if len(gravity) != 3 or any(abs(a - b) > 1e-3 for a, b in zip(gravity, EXPECTED_GRAVITY)):
        raise VerifierFailure(f"la gravedad debería ser {EXPECTED_GRAVITY}, es {gravity}")

    models = [m for m in world.findall("model") if m.get("name") != "robot_delivery"]
    static_extra = [m for m in models if (m.find("static") is not None and m.find("static").text == "true")]
    if not static_extra:
        raise VerifierFailure("no se ha encontrado ningún objeto estático adicional en el mundo")


def main():
    run_verifier("verificador_tema4_ej6", 6, check)


if __name__ == "__main__":
    main()
