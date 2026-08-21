import os
import time

from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    run_verifier,
    student_repo_path,
    wait_for_node,
    wait_for_topic_type,
)

NAMESPACE = "/robot1"
NODES = ["nodo_tf_estatico", "nodo_tf_dinamico", "nodo_tf_listener"]


def check(node):
    for name in NODES:
        wait_for_node(node, name, namespace=NAMESPACE)
    wait_for_topic_type(node, "/tf", "tf2_msgs/msg/TFMessage")
    wait_for_topic_type(node, "/tf_static", "tf2_msgs/msg/TFMessage")

    # La ruta/nombre exacto del bag de esta grabación automática no está mandatado
    # por el enunciado del Ej.9 (solo lo está en el Ej.6); nos limitamos a
    # comprobar que 'bags/' recibe actividad nueva durante el lanzamiento.
    bags_dir = os.path.join(student_repo_path(node), "bags")
    before = set(os.listdir(bags_dir)) if os.path.isdir(bags_dir) else set()
    time.sleep(3.0)
    after = set(os.listdir(bags_dir)) if os.path.isdir(bags_dir) else set()
    if not (after - before) and not after:
        raise VerifierFailure(
            "no se observa ninguna grabación nueva en 'bags/' durante el lanzamiento de integración"
        )


def main():
    run_verifier("verificador_tema3_ej9", 9, check)


if __name__ == "__main__":
    main()
