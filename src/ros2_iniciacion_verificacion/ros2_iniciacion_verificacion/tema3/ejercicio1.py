from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    require_file,
    run_verifier,
    student_repo_path,
)

MIT_MARKERS = ("MIT License", "Permission is hereby granted")


def check(node):
    repo = student_repo_path(node)
    path = require_file(repo, "LICENSE")
    text = open(path, encoding="utf-8").read()
    if not all(marker in text for marker in MIT_MARKERS):
        raise VerifierFailure("LICENSE no contiene el texto estándar de la licencia MIT")


def main():
    run_verifier("verificador_tema3_ej1", 1, check)


if __name__ == "__main__":
    main()
