from std_srvs.srv import Trigger

from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, call_service, run_verifier


def check(node):
    response = call_service(node, "/robot1/reiniciar_sistema", Trigger, Trigger.Request())
    if not response.success:
        raise VerifierFailure("se esperaba success=true en la respuesta de /robot1/reiniciar_sistema")
    if "reiniciado" not in response.message.lower():
        raise VerifierFailure(f"mensaje de respuesta inesperado: '{response.message}'")


def main():
    run_verifier("verificador_tema5_ej8", 8, check)


if __name__ == "__main__":
    main()
