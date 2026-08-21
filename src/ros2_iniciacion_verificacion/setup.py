import os
from glob import glob

from setuptools import find_packages, setup

package_name = "ros2_iniciacion_verificacion"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name, "launch"), glob("launch/*.launch.py")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Francisco José Mañas Álvarez",
    maintainer_email="fma527@ual.es",
    description=(
        "Nodos, launch files y configuración para la validación automática de los "
        "ejercicios de los Temas 2-5 de Introducción a la Robótica con ROS 2 (UNED)."
    ),
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            # Tema 2
            "verificador_tema2_ej1 = ros2_iniciacion_verificacion.tema2.ejercicio1:main",
            "verificador_tema2_ej2 = ros2_iniciacion_verificacion.tema2.ejercicio2:main",
            "verificador_tema2_ej3 = ros2_iniciacion_verificacion.tema2.ejercicio3:main",
            "verificador_tema2_ej4 = ros2_iniciacion_verificacion.tema2.ejercicio4:main",
            "verificador_tema2_ej5 = ros2_iniciacion_verificacion.tema2.ejercicio5:main",
            "verificador_tema2_ej6 = ros2_iniciacion_verificacion.tema2.ejercicio6:main",
            "verificador_tema2_ej7 = ros2_iniciacion_verificacion.tema2.ejercicio7:main",
            "verificador_tema2_ej8 = ros2_iniciacion_verificacion.tema2.ejercicio8:main",
            "verificador_tema2_ej9 = ros2_iniciacion_verificacion.tema2.ejercicio9:main",
            "mock_estacion_carga = ros2_iniciacion_verificacion.tema2.mock_estacion_carga:main",
            "mock_navegacion = ros2_iniciacion_verificacion.tema2.mock_navegacion:main",
            # Tema 3
            "verificador_tema3_ej1 = ros2_iniciacion_verificacion.tema3.ejercicio1:main",
            "verificador_tema3_ej2 = ros2_iniciacion_verificacion.tema3.ejercicio2:main",
            "verificador_tema3_ej3 = ros2_iniciacion_verificacion.tema3.ejercicio3:main",
            "verificador_tema3_ej4 = ros2_iniciacion_verificacion.tema3.ejercicio4:main",
            "verificador_tema3_ej5 = ros2_iniciacion_verificacion.tema3.ejercicio5:main",
            "verificador_tema3_ej6 = ros2_iniciacion_verificacion.tema3.ejercicio6:main",
            "verificador_tema3_ej7 = ros2_iniciacion_verificacion.tema3.ejercicio7:main",
            "verificador_tema3_ej8 = ros2_iniciacion_verificacion.tema3.ejercicio8:main",
            "verificador_tema3_ej9 = ros2_iniciacion_verificacion.tema3.ejercicio9:main",
            "mock_tf_dinamico = ros2_iniciacion_verificacion.tema3.mock_tf_dinamico:main",
            # Tema 4
            "verificador_tema4_ej1 = ros2_iniciacion_verificacion.tema4.ejercicio1:main",
            "verificador_tema4_ej2 = ros2_iniciacion_verificacion.tema4.ejercicio2:main",
            "verificador_tema4_ej3 = ros2_iniciacion_verificacion.tema4.ejercicio3:main",
            "verificador_tema4_ej4 = ros2_iniciacion_verificacion.tema4.ejercicio4:main",
            "verificador_tema4_ej5 = ros2_iniciacion_verificacion.tema4.ejercicio5:main",
            "verificador_tema4_ej6 = ros2_iniciacion_verificacion.tema4.ejercicio6:main",
            "verificador_tema4_ej7 = ros2_iniciacion_verificacion.tema4.ejercicio7:main",
            "verificador_tema4_ej8 = ros2_iniciacion_verificacion.tema4.ejercicio8:main",
            "verificador_tema4_ej9 = ros2_iniciacion_verificacion.tema4.ejercicio9:main",
            # Tema 5
            "verificador_tema5_ej1 = ros2_iniciacion_verificacion.tema5.ejercicio1:main",
            "verificador_tema5_ej2 = ros2_iniciacion_verificacion.tema5.ejercicio2:main",
            "verificador_tema5_ej3 = ros2_iniciacion_verificacion.tema5.ejercicio3:main",
            "verificador_tema5_ej4 = ros2_iniciacion_verificacion.tema5.ejercicio4:main",
            "verificador_tema5_ej5 = ros2_iniciacion_verificacion.tema5.ejercicio5:main",
            "verificador_tema5_ej6 = ros2_iniciacion_verificacion.tema5.ejercicio6:main",
            "verificador_tema5_ej7 = ros2_iniciacion_verificacion.tema5.ejercicio7:main",
            "verificador_tema5_ej8 = ros2_iniciacion_verificacion.tema5.ejercicio8:main",
            "verificador_tema5_ej9 = ros2_iniciacion_verificacion.tema5.ejercicio9:main",
        ],
    },
)
