from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, find_package_share_file, run_verifier

REQUIRED_PLUGINS = ["rqt_graph", "rqt_topic_monitor"]


def check(node):
    # El formato de los ficheros .perspective de rqt es un serializado propio de
    # qt_gui.settings, no XML/JSON documentado; nos limitamos a buscar los
    # nombres de plugin exigidos como subcadenas, que es lo que el enunciado
    # pide comprobar ("que referencia los plugins solicitados").
    path = find_package_share_file("tema5_practica", "config/tema5.perspective")
    text = open(path, encoding="utf-8").read()
    missing = [p for p in REQUIRED_PLUGINS if p not in text]
    if missing:
        raise VerifierFailure(f"config/tema5.perspective no referencia los plugins: {missing}")


def main():
    run_verifier("verificador_tema5_ej2", 2, check)


if __name__ == "__main__":
    main()
