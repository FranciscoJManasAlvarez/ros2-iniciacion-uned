from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    collect_messages,
    run_verifier,
    wait_for_topic_type,
)

REQUIRED_FIELDS = {"bateria": "float", "estado": "string", "x": "float", "y": "float"}
ESTADOS_VALIDOS = {"EN_REPARTO", "CARGANDO", "INACTIVO"}


def check(node):
    try:
        from tema2_practica_interfaces.msg import EstadoRobot
    except ImportError as exc:
        raise VerifierFailure(
            "no se puede importar tema2_practica_interfaces.msg.EstadoRobot "
            f"(¿está el paquete de interfaces compilado en este workspace?): {exc}"
        )

    fields = EstadoRobot.get_fields_and_field_types()
    for field, expected in REQUIRED_FIELDS.items():
        if field not in fields:
            raise VerifierFailure(f"EstadoRobot.msg no tiene el campo '{field}'")
        if expected not in fields[field]:
            raise VerifierFailure(
                f"EstadoRobot.msg campo '{field}' esperado tipo '{expected}', es '{fields[field]}'"
            )

    wait_for_topic_type(node, "/robot/estado", "tema2_practica_interfaces/msg/EstadoRobot")
    msgs = collect_messages(node, "/robot/estado", EstadoRobot, count=1, timeout=6.0)
    if msgs[0].estado not in ESTADOS_VALIDOS:
        raise VerifierFailure(f"'estado' debería ser uno de {ESTADOS_VALIDOS}, es '{msgs[0].estado}'")


def main():
    run_verifier("verificador_tema2_ej4", 4, check)


if __name__ == "__main__":
    main()
