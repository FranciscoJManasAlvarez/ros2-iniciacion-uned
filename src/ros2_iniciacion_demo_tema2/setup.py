from glob import glob
from setuptools import setup, find_packages

package_name = "ros2_iniciacion_demo_tema2"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name + "/launch", glob("launch/*.launch.py")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Francisco José Mañas Álvarez",
    maintainer_email="fma527@ual.es",
    description="Demos de topics/servicios/acciones (Tema 2)",
    license="MIT",
    entry_points={
        "console_scripts": [
            "nodo_sensor_temperatura = ros2_iniciacion_demo_tema2.nodo_sensor_temperatura:main",
            "nodo_estacion_acoplamiento = ros2_iniciacion_demo_tema2.nodo_estacion_acoplamiento:main",
        ],
    },
)
