# ros2_iniciacion_demo_tema4

Demo de modelado URDF/XACRO y mundo Gazebo de un robot distinto al evaluado
(`robot_delivery`): un mástil de sensores con cámara, para practicar el flujo
de trabajo del Tema 4 sin anticipar la solución de `tema4_practica`.

## Contenido

- `urdf/mastil_sensores.urdf.xacro`: base + mástil + cámara, con bloque
  `<gazebo>` de sensor tipo `camera`.
- `worlds/patio.sdf`: mundo Gazebo mínimo (gravedad + suelo + un banco estático).
- `launch/ver_mastil.launch.py`: `robot_state_publisher` + `joint_state_publisher`
  + `rviz2` para visualizar el modelo (equivalente de demo al Ej.5 evaluado).

## Uso

```bash
ros2 launch ros2_iniciacion_demo_tema4 ver_mastil.launch.py
```

Para simularlo en Gazebo con `ros_gz_sim` (requiere Gazebo instalado):

```bash
ros2 launch ros_gz_sim gz_sim.launch.py gz_args:="-r $(ros2 pkg prefix ros2_iniciacion_demo_tema4)/share/ros2_iniciacion_demo_tema4/worlds/patio.sdf"
ros2 run ros_gz_sim create -name mastil_sensores -topic robot_description
ros2 run ros_gz_bridge parameter_bridge /camera@sensor_msgs/msg/Image[gz.msgs.Image
```
