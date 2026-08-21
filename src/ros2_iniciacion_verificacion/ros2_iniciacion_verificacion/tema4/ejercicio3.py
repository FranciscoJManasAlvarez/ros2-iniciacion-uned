from ros2_iniciacion_verificacion.tema4.urdf_utils import find_link, find_share_file, process_xacro_file
from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, run_verifier


def _wheel_radius(root, link_name):
    link = find_link(root, link_name)
    if link is None:
        raise VerifierFailure(f"falta el link '{link_name}' tras procesar el xacro")
    cylinder = link.find("visual/geometry/cylinder")
    if cylinder is None:
        raise VerifierFailure(f"'{link_name}' debería tener geometría <cylinder> generada por la macro 'wheel'")
    return float(cylinder.get("radius"))


def check(node):
    path = find_share_file("tema4_practica", "urdf/robot_delivery.urdf.xacro")

    default_root = process_xacro_file(path)
    r_left_default = _wheel_radius(default_root, "left_wheel_link")
    r_right_default = _wheel_radius(default_root, "right_wheel_link")
    if abs(r_left_default - 0.08) > 1e-3 or abs(r_right_default - 0.08) > 1e-3:
        raise VerifierFailure(
            f"con 'wheel_radius' por defecto (0.08) se esperaba radio 0.08 en ambas ruedas, "
            f"se ha obtenido {r_left_default}/{r_right_default}"
        )

    override_root = process_xacro_file(path, mappings={"wheel_radius": "0.2"})
    r_left_override = _wheel_radius(override_root, "left_wheel_link")
    if abs(r_left_override - 0.2) > 1e-3:
        raise VerifierFailure(
            "la propiedad 'wheel_radius' no parece controlar el radio de la macro 'wheel' "
            f"(al fijarla a 0.2 se ha obtenido {r_left_override})"
        )


def main():
    run_verifier("verificador_tema4_ej3", 3, check)


if __name__ == "__main__":
    main()
