"""Demo de servicio: estación de acoplamiento (docking) de RobotDelivery.
Mismo patrón que nodo_estacion_carga (Ej.5 evaluado) con otro servicio, para
que se pueda practicar cliente/servidor sin tocar la interfaz del ejercicio.
"""
import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger


class NodoEstacionAcoplamiento(Node):
    def __init__(self):
        super().__init__("nodo_estacion_acoplamiento")
        self.create_service(Trigger, "/robot/solicitar_acoplamiento", self._on_request)

    def _on_request(self, request, response):
        response.success = True
        response.message = "Acoplamiento completado"
        return response


def main():
    rclpy.init()
    try:
        rclpy.spin(NodoEstacionAcoplamiento())
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()
