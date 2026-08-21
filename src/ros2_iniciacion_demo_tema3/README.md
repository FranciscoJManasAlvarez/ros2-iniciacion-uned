# ros2_iniciacion_demo_tema3

Demo de TF estática/dinámica sobre RobotDelivery, con nombres de frame
distintos a los del ejercicio evaluado (`tema3_practica`), más una guía
rápida de `rosbag`.

## Nodos

- `nodo_tf_soporte_camara`: TF estática `base_link -> camera_mount_frame`.
- `nodo_tf_brazo`: TF dinámica `base_link -> gripper_joint_frame` (oscilación).

## Lanzamiento

```bash
ros2 launch ros2_iniciacion_demo_tema3 demo_tema3.launch.py
```

## Guía rápida de rosbag

```bash
# Grabar (10+ s) los topics de TF mientras corre la demo:
ros2 bag record /tf /tf_static -o mi_grabacion

# Inspeccionar la grabación:
ros2 bag info mi_grabacion

# Reproducirla:
ros2 bag play mi_grabacion
```
