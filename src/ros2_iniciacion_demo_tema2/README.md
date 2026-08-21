# ros2_iniciacion_demo_tema2

Demos ilustrativas de publisher/parámetro dinámico y servicio, sobre el mismo
escenario RobotDelivery del Tema 2, con nombres distintos a los del ejercicio
evaluado (`tema2_practica`) para no anticipar su solución.

## Nodos

- `nodo_sensor_temperatura`: publica `/robot/temperatura_carga` (Float32, 1 Hz),
  configurable con el parámetro `temperatura_ambiente`.
- `nodo_estacion_acoplamiento`: sirve `/robot/solicitar_acoplamiento` (`std_srvs/Trigger`).

## Lanzamiento

```bash
ros2 launch ros2_iniciacion_demo_tema2 demo_tema2.launch.py
```
