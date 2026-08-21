import os
import re
import subprocess

from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, run_verifier, student_repo_path

MIN_DURATION_S = 10.0
REQUIRED_TOPICS = {"/tf", "/tf_static"}


def check(node):
    repo = student_repo_path(node)
    bag_path = os.path.join(repo, "bags", "tema3_bag")
    if not os.path.isdir(bag_path) and not os.path.isfile(bag_path):
        raise VerifierFailure(f"no se encuentra la grabación en '{bag_path}'")

    result = subprocess.run(
        ["ros2", "bag", "info", bag_path], capture_output=True, text=True, timeout=30
    )
    if result.returncode != 0:
        raise VerifierFailure(f"'ros2 bag info' ha fallado: {result.stderr.strip()}")

    output = result.stdout
    topics_found = set(re.findall(r"Topic:\s*(\S+)", output))
    missing = REQUIRED_TOPICS - topics_found
    if missing:
        raise VerifierFailure(f"la grabación no contiene los topics {missing} (encontrados: {topics_found})")

    duration_match = re.search(r"Duration:\s*([\d.]+)", output)
    if not duration_match or float(duration_match.group(1)) < MIN_DURATION_S:
        raise VerifierFailure(
            f"la grabación debe durar al menos {MIN_DURATION_S}s "
            f"(reportado: {duration_match.group(1) if duration_match else 'desconocido'})"
        )


def main():
    run_verifier("verificador_tema3_ej6", 6, check)


if __name__ == "__main__":
    main()
