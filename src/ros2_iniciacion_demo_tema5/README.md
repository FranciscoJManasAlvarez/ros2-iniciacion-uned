# ros2_iniciacion_demo_tema5

Demos de supervisión/interfaz sobre RobotDelivery, con nombres distintos a los
del ejercicio evaluado (`tema5_practica`).

## Contenido

- `nodo_gui_pyqt_demo`: ventana PyQt5 mínima con un botón que publica
  `/robot/aviso_mantenimiento` (String) — mismo patrón que el Ej.6-7 evaluado.
- `config/`: pensada para que guardes aquí tus propias perspectivas RQT /
  configuraciones RViz de práctica, sin tocar `config/tema5.*` del ejercicio.
- `launch/demo_foxglove.launch.py`: arranca `foxglove_bridge` de forma aislada
  para probar la conexión desde Foxglove Studio.

## Uso

```bash
ros2 run ros2_iniciacion_demo_tema5 nodo_gui_pyqt_demo
ros2 launch ros2_iniciacion_demo_tema5 demo_foxglove.launch.py
```
