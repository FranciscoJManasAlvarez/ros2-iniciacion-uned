"""Demo de publisher + parámetro dinámico: sensor de temperatura del compartimento
de carga de RobotDelivery. Mismo patrón que nodo_sensor (Ej.2 evaluado), aplicado
a otra magnitud, para practicar el patrón sin reutilizar el ejercicio calificado.
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class NodoSensorTemperatura(Node):
    def __init__(self):
        super().__init__("nodo_sensor_temperatura")
        self.declare_parameter("temperatura_ambiente", 20.0)
        self._pub = self.create_publisher(Float32, "/robot/temperatura_carga", 10)
        self.create_timer(1.0, self._tick)

    def _tick(self):
        ambiente = self.get_parameter("temperatura_ambiente").value
        self._pub.publish(Float32(data=ambiente))


def main():
    rclpy.init()
    try:
        rclpy.spin(NodoSensorTemperatura())
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()
