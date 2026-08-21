from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    run_verifier,
    send_action_goal,
    wait_for_node,
)


def check(node):
    try:
        from tema2_practica_interfaces.action import Desplazarse
    except ImportError as exc:
        raise VerifierFailure(f"no se puede importar tema2_practica_interfaces.action.Desplazarse: {exc}")

    wait_for_node(node, "mock_estacion_carga")

    goal = Desplazarse.Goal(distancia_objetivo=5.0)
    feedback, result = send_action_goal(node, "/robot/desplazarse", Desplazarse, goal, timeout=15.0)

    if len(feedback) != 5:
        raise VerifierFailure(f"se esperaban exactamente 5 mensajes de feedback, se han recibido {len(feedback)}")
    restantes = [fb.iteraciones_restantes for fb in feedback]
    if restantes != [4, 3, 2, 1, 0]:
        raise VerifierFailure(f"'iteraciones_restantes' debería decrecer 4..0, ha sido {restantes}")
    if not result.exito:
        raise VerifierFailure("se esperaba exito=true en el resultado final")
    if abs(result.distancia_total - 5.0) > 1e-3:
        raise VerifierFailure(f"'distancia_total' debería ser 5.0, es {result.distancia_total}")


def main():
    run_verifier("verificador_tema2_ej7", 7, check)


if __name__ == "__main__":
    main()
