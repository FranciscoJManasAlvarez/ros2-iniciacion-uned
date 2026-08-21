# ros2-iniciacion-uned

Repositorio de apoyo del curso de Formación Permanente UNED **"Introducción a
la Robótica con ROS 2"**: contiene el paquete que valida automáticamente los
ejercicios evaluados de cada tema, y una serie de paquetes de demostración
que ilustran conceptos del curso sin sustituir a la práctica evaluada.

## Descripción

A lo largo del curso, cada práctica pide construir el software de control de
un robot de reparto autónomo ficticio, **RobotDelivery**, con nombres de
paquete/nodo/topic/servicio/acción exigidos exactamente por el enunciado.
Este repositorio proporciona el lanzador y el nodo verificador de cada
ejercicio, para que puedas comprobar tu propia solución antes de entregarla.

## Requisitos

- ROS 2 Humble (Ubuntu 22.04).
- `colcon` y las herramientas estándar de desarrollo ROS 2.
- Para los ejercicios de Gazebo del Tema 4 (Ej. 6-9): `ros_gz_sim` / `ros_gz_bridge`.
- Para el Tema 5: `rqt`, `rviz2`, `foxglove_bridge`, `PyQt5`.

## Instalación

Clona este repositorio **dentro del mismo workspace** donde tengas (o vayas a
tener) tus propios paquetes de solución (`tema2_practica`,
`tema2_practica_interfaces`, `tema3_practica`, `tema4_practica`,
`tema5_practica`):

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone https://github.com/FranciscoJManasAlvarez/ros2-iniciacion-uned.git
# ... coloca aquí también tus propios paquetes de solución ...
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

## Uso

Para validar el Ejercicio N del Tema X:

```bash
ros2 launch ros2_iniciacion_verificacion temaXejercicioN.launch.py
```

Si todo es correcto verás `[verificador]: OK - Ejercicio N superado
correctamente` y la red ROS 2 se cerrará automáticamente. Si no, verás un
mensaje `[verificador]: FAIL - <motivo>` con el diagnóstico concreto.

Los ejercicios de comprobación de ficheros (LICENSE, README.md, `docs/`, en
el Tema 3, Ej. 1/2/8) necesitan además la ruta a la raíz de **tu propio**
repositorio de solución, vía el argumento `student_repo_path` (por defecto,
el directorio desde el que lances el comando):

```bash
ros2 launch ros2_iniciacion_verificacion tema3ejercicio1.launch.py student_repo_path:=/ruta/a/tu/repo
```

Los paquetes `ros2_iniciacion_demo_temaN` no forman parte de la evaluación:
son demos ilustrativas del mismo escenario RobotDelivery, con nombres de
nodo/topic distintos a los del ejercicio evaluado correspondiente, pensadas
para practicar un patrón antes de aplicarlo en tu propia solución. Cada una
tiene su propio README.

## Estructura del repositorio

```
src/
├── ros2_iniciacion_verificacion/    # Verificación automática de Temas 2-5 (Tema 1 pendiente, ver Notas)
├── ros2_iniciacion_demo_tema2/      # Demo: topics, parámetros, servicios
├── ros2_iniciacion_demo_tema3/      # Demo: TF estática/dinámica + guía de rosbag
├── ros2_iniciacion_demo_tema4/      # Demo: URDF/XACRO + mundo Gazebo
└── ros2_iniciacion_demo_tema5/      # Demo: interfaz PyQt + foxglove_bridge
```

## Notas

- **El Tema 1 no tiene paquete de validación todavía**: `tema1_ejercicios.tex`
  es, a día de hoy, un placeholder sin ejercicios reales definidos (solo un
  "Ejercicio 1: TO-DO"). Se añadirá cuando el enunciado esté completo.
- **Tema 4, Ej. 6-9 (Gazebo)**: requieren `ros_gz_sim`/`ros_gz_bridge`
  instalados; si no lo están, el verificador falla con un diagnóstico claro
  en vez de quedarse esperando indefinidamente.
- **Tema 5, Ej. 6-7 (botón PyQt)**: el enunciado prevé simular la pulsación
  del botón con `QTest`, lo que exige un punto de entrada de clase conocido
  que el enunciado no fija. A falta de esa convención, la comprobación
  automática se limita a la interfaz pública observable (nodo vivo,
  publicador/suscriptor correctos); formalizar dicho punto de entrada queda
  pendiente para una futura revisión del enunciado.
- **Tema 3, Ej. 9 (grabación automática de integración)**: el enunciado no
  fija el nombre/ruta exacta del bag en el lanzador de integración (a
  diferencia del Ej. 6); el verificador comprueba que `bags/` recibe
  actividad nueva durante el lanzamiento.

## Licencia

MIT. Ver [LICENSE](LICENSE).
