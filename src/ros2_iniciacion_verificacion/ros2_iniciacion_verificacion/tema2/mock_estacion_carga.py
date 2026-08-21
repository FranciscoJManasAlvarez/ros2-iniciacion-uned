"""Doble de pruebas de nodo_estacion_carga (Ej.5), usado para aislar a los
nodos cliente (nodo_monitor en Ej.6, nodo_navegacion en Ej.7) del resto del
sistema. Cada petición atendida se cuenta y se publica en /mock/solicitar_carga_calls
para que el verificador pueda comprobar, sin acoplarse al proceso, cuántas
veces se ha llamado al servicio.
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from tema2_practica_interfaces.srv import SolicitarCarga


class MockEstacionCarga(Node):
    def __init__(self):
        super().__init__("mock_estacion_carga")
        self._count = 0
        self._counter_pub = self.create_publisher(Int32, "/mock/solicitar_carga_calls", 10)
        self.create_service(SolicitarCarga, "/robot/solicitar_carga", self._on_request)

    def _on_request(self, request, response):
        self._count += 1
        self._counter_pub.publish(Int32(data=self._count))
        response.aceptado = True
        response.mensaje = "Carga concedida"
        return response


def main():
    rclpy.init()
    node = MockEstacionCarga()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
