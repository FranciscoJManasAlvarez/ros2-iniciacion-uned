from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, call_service, run_verifier


def check(node):
    try:
        from tema2_practica_interfaces.srv import SolicitarCarga
    except ImportError as exc:
        raise VerifierFailure(f"no se puede importar tema2_practica_interfaces.srv.SolicitarCarga: {exc}")

    request = SolicitarCarga.Request(bateria_actual=10.0)
    response = call_service(node, "/robot/solicitar_carga", SolicitarCarga, request)
    if not response.aceptado:
        raise VerifierFailure("se esperaba aceptado=true en la respuesta de /robot/solicitar_carga")
    if not response.mensaje:
        raise VerifierFailure("se esperaba un 'mensaje' no vacío en la respuesta")


def main():
    run_verifier("verificador_tema2_ej5", 5, check)


if __name__ == "__main__":
    main()
