from std_msgs.msg import Float32

from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    collect_messages,
    run_verifier,
    set_remote_param,
    wait_for_topic_type,
)

PARAMETER_DOUBLE = 3


def check(node):
    wait_for_topic_type(node, "/robot/bateria", "std_msgs/msg/Float32")

    baseline = collect_messages(node, "/robot/bateria", Float32, count=3, timeout=6.0)
    values = [m.data for m in baseline]
    if not all(0.0 <= v <= 100.0 for v in values):
        raise VerifierFailure("los valores de batería deben estar entre 0.0 y 100.0")
    if not (values[0] >= values[-1]):
        raise VerifierFailure("la batería debería decrecer (o mantenerse) con el tiempo")

    set_remote_param(node, "/nodo_sensor", "velocidad_descarga", 20.0, PARAMETER_DOUBLE)
    fast = collect_messages(node, "/robot/bateria", Float32, count=3, timeout=6.0)
    fast_values = [m.data for m in fast]
    if len(fast_values) >= 2 and (fast_values[0] - fast_values[-1]) <= (values[0] - values[-1]):
        raise VerifierFailure(
            "al aumentar 'velocidad_descarga' el ritmo de descarga observado no ha aumentado"
        )


def main():
    run_verifier("verificador_tema2_ej2", 2, check)


if __name__ == "__main__":
    main()
