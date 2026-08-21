import yaml

from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, find_package_share_file, run_verifier

REQUIRED_DISPLAY_CLASSES = ["LaserScan", "Odometry", "TF"]


def check(node):
    path = find_package_share_file("tema5_practica", "config/tema5.rviz")
    try:
        config = yaml.safe_load(open(path, encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise VerifierFailure(f"config/tema5.rviz no es un YAML válido: {exc}")

    viz_manager = (config or {}).get("Visualization Manager", {})
    displays = viz_manager.get("Displays", [])
    classes = " ".join(str(d.get("Class", "")) for d in displays)
    missing = [c for c in REQUIRED_DISPLAY_CLASSES if c not in classes]
    if missing:
        raise VerifierFailure(f"config/tema5.rviz no incluye displays de tipo: {missing}")

    fixed_frame = viz_manager.get("Global Options", {}).get("Fixed Frame")
    if fixed_frame != "odom":
        raise VerifierFailure(f"'Fixed Frame' debería ser 'odom', es '{fixed_frame}'")


def main():
    run_verifier("verificador_tema5_ej3", 3, check)


if __name__ == "__main__":
    main()
