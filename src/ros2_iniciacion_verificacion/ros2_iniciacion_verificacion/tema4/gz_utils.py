"""Ayudas mínimas para interrogar una simulación Gazebo (ros_gz) en marcha.

Los ejercicios 7-9 solo pueden verificarse con Gazebo realmente instalado; si
no lo está, se falla con un diagnóstico claro (ver `require_command('gz')` en
verifier_base) en lugar de colgarse esperando algo que nunca va a aparecer.
"""
import subprocess

from ros2_iniciacion_verificacion.verifier_base import VerifierFailure

CANDIDATE_WORLDS = ["almacen", "default"]


def entity_pose(model_name, timeout=20.0):
    """Intenta obtener la pose de `model_name` vía `gz service -s /world/<w>/state`."""
    last_error = None
    for world in CANDIDATE_WORLDS:
        try:
            result = subprocess.run(
                [
                    "gz",
                    "service",
                    "-s",
                    f"/world/{world}/state",
                    "--reqtype",
                    "gz.msgs.Empty",
                    "--reptype",
                    "gz.msgs.SerializedStepMap",
                    "--timeout",
                    str(int(timeout * 1000)),
                    "--req",
                    "",
                ],
                capture_output=True,
                text=True,
                timeout=timeout + 5,
            )
        except (subprocess.TimeoutExpired, FileNotFoundError) as exc:
            last_error = str(exc)
            continue
        if result.returncode == 0 and model_name in result.stdout:
            return _parse_position(result.stdout, model_name)
        last_error = result.stderr.strip() or f"mundo '{world}' no disponible"
    raise VerifierFailure(f"no se ha podido consultar la pose de '{model_name}' en Gazebo: {last_error}")


def _parse_position(raw_state, model_name):
    # El formato de texto de `gz service` no es JSON estable entre versiones;
    # nos limitamos a intentar extraer x/y/z con una búsqueda tolerante.
    try:
        idx = raw_state.index(model_name)
        chunk = raw_state[idx : idx + 400]
        x = float(chunk.split("x:")[1].split()[0])
        y = float(chunk.split("y:")[1].split()[0])
        z = float(chunk.split("z:")[1].split()[0])
        return (x, y, z)
    except (ValueError, IndexError) as exc:
        raise VerifierFailure(f"no se ha podido interpretar la pose de '{model_name}': {exc}")
