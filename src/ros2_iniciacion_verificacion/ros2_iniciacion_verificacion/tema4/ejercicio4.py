from ros2_iniciacion_verificacion.tema4.urdf_utils import find_joint, find_link, find_share_file, process_xacro_file
from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, run_verifier


def check(node):
    path = find_share_file("tema4_practica", "urdf/robot_delivery.urdf.xacro")
    root = process_xacro_file(path)

    if find_link(root, "lidar_link") is None:
        raise VerifierFailure("falta el link 'lidar_link'")

    joint = find_joint(root, "lidar_joint")
    if joint is None:
        raise VerifierFailure("falta el joint 'lidar_joint'")
    if joint.get("type") != "fixed":
        raise VerifierFailure("'lidar_joint' debería ser de tipo 'fixed'")
    parent = joint.find("parent")
    if parent is None or parent.get("link") != "base_link":
        raise VerifierFailure("'lidar_joint' debería tener 'base_link' como parent")

    gazebo_block = None
    for gazebo in root.findall("gazebo"):
        if gazebo.get("reference") == "lidar_link":
            gazebo_block = gazebo
            break
    if gazebo_block is None:
        raise VerifierFailure("falta el bloque <gazebo reference=\"lidar_link\">")

    sensor = gazebo_block.find("sensor")
    if sensor is None or sensor.get("type") != "ray":
        raise VerifierFailure("el sensor de 'lidar_link' debería ser de tipo 'ray'")

    update_rate = sensor.find("update_rate")
    if update_rate is None or abs(float(update_rate.text) - 10.0) > 1e-6:
        raise VerifierFailure("el sensor LIDAR debería tener update_rate=10")

    samples = sensor.find("ray/scan/horizontal/samples")
    if samples is None or int(samples.text) != 360:
        raise VerifierFailure("el sensor LIDAR debería tener 360 muestras")

    rng = sensor.find("ray/range")
    if rng is None:
        raise VerifierFailure("falta el bloque <range> del sensor LIDAR")
    rmin, rmax = float(rng.find("min").text), float(rng.find("max").text)
    if abs(rmin - 0.12) > 1e-3 or abs(rmax - 10.0) > 1e-3:
        raise VerifierFailure(f"el rango del LIDAR debería ser 0.12-10.0 m, es {rmin}-{rmax}")


def main():
    run_verifier("verificador_tema4_ej4", 4, check)


if __name__ == "__main__":
    main()
