"""Doble de pruebas de nodo_navegacion (Ej.7), usado en Ej.8 para aislar al
cliente de la acción (nodo_hola) del resto del sistema. Simula directamente
las 5 iteraciones de feedback sin depender del servicio de carga, y publica
la distancia objetivo recibida en /mock/navegacion_goal_distancia para que el
verificador confirme, desde fuera, que el goal recibido era el esperado.
"""
import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from std_msgs.msg import Float32
from tema2_practica_interfaces.action import Desplazarse


class MockNavegacion(Node):
    def __init__(self):
        super().__init__("mock_navegacion")
        self._goal_pub = self.create_publisher(Float32, "/mock/navegacion_goal_distancia", 10)
        ActionServer(self, Desplazarse, "/robot/desplazarse", self._execute)

    def _execute(self, goal_handle):
        objetivo = goal_handle.request.distancia_objetivo
        self._goal_pub.publish(Float32(data=objetivo))
        feedback = Desplazarse.Feedback()
        for restante in (4, 3, 2, 1, 0):
            feedback.iteraciones_restantes = restante
            feedback.distancia_recorrida = objetivo * (5 - restante) / 5.0
            goal_handle.publish_feedback(feedback)
            time.sleep(0.2)
        goal_handle.succeed()
        result = Desplazarse.Result()
        result.exito = True
        result.distancia_total = objetivo
        return result


def main():
    rclpy.init()
    node = MockNavegacion()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
