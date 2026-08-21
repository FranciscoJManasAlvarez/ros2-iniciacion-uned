"""Demo mínima de interfaz PyQt5 + rclpy: un botón que publica un aviso de
mantenimiento. Mismo patrón que nodo_gui_pyqt (Ej.6-7 evaluados) con otro
topic/mensaje, para practicar la integración Qt+ROS sin tocar el ejercicio.
"""
import sys
import threading

import rclpy
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from rclpy.node import Node
from std_msgs.msg import String


class NodoGuiPyqtDemo(Node):
    def __init__(self):
        super().__init__("nodo_gui_pyqt_demo")
        self._pub = self.create_publisher(String, "/robot/aviso_mantenimiento", 10)

    def enviar_aviso(self):
        self._pub.publish(String(data="REVISAR_RUEDAS"))


class VentanaDemo(QWidget):
    def __init__(self, node):
        super().__init__()
        self._node = node
        self.setWindowTitle("Demo PyQt - RobotDelivery")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Panel de mantenimiento (demo)"))
        boton = QPushButton("Enviar aviso de mantenimiento")
        boton.clicked.connect(self._node.enviar_aviso)
        layout.addWidget(boton)
        self.setLayout(layout)


def main():
    rclpy.init()
    node = NodoGuiPyqtDemo()
    threading.Thread(target=rclpy.spin, args=(node,), daemon=True).start()

    app = QApplication(sys.argv)
    ventana = VentanaDemo(node)
    ventana.show()
    app.exec_()

    rclpy.try_shutdown()


if __name__ == "__main__":
    main()
