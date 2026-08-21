import glob
import os

from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, require_file, run_verifier, student_repo_path


def check(node):
    repo = student_repo_path(node)
    docs_dir = os.path.join(repo, "docs")
    if not os.path.isdir(docs_dir):
        raise VerifierFailure("no existe la carpeta 'docs/' en la raíz del repositorio")

    html_files = glob.glob(os.path.join(docs_dir, "*.html"))
    if len(html_files) < 3:
        raise VerifierFailure(f"se esperaban al menos 3 ficheros .html en docs/, hay {len(html_files)}")

    require_file(repo, os.path.join("docs", "assets", "style.css"))

    linked_css = 0
    cross_links = 0
    names = {os.path.basename(f) for f in html_files}
    for f in html_files:
        text = open(f, encoding="utf-8").read()
        if "assets/style.css" in text:
            linked_css += 1
        if any(other in text for other in names if other != os.path.basename(f)):
            cross_links += 1

    if linked_css < len(html_files):
        raise VerifierFailure("no todas las páginas HTML referencian docs/assets/style.css")
    if cross_links == 0:
        raise VerifierFailure("las páginas HTML no parecen estar enlazadas entre sí mediante un menú")


def main():
    run_verifier("verificador_tema3_ej8", 8, check)


if __name__ == "__main__":
    main()
