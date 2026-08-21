import re

from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    require_file,
    run_verifier,
    student_repo_path,
)

REQUIRED_SECTIONS = [
    "Descripción",
    "Requisitos",
    "Instalación",
    "Uso",
    "Estructura del repositorio",
    "Licencia",
]


def check(node):
    repo = student_repo_path(node)
    path = require_file(repo, "README.md")
    text = open(path, encoding="utf-8").read()
    headings = set(re.findall(r"^#{1,6}\s*(.+?)\s*$", text, flags=re.MULTILINE))
    missing = [s for s in REQUIRED_SECTIONS if s not in headings]
    if missing:
        raise VerifierFailure(f"README.md no incluye las secciones: {', '.join(missing)}")


def main():
    run_verifier("verificador_tema3_ej2", 2, check)


if __name__ == "__main__":
    main()
