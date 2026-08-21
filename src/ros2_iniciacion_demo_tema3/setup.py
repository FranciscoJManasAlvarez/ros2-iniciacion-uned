from glob import glob
from setuptools import setup, find_packages

package_name = "ros2_iniciacion_demo_tema3"

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
    description="Demo de TF y guía de rosbag (Tema 3)",
    license="MIT",
    entry_points={
        "console_scripts": [
            "nodo_tf_soporte_camara = ros2_iniciacion_demo_tema3.nodo_tf_soporte_camara:main",
            "nodo_tf_brazo = ros2_iniciacion_demo_tema3.nodo_tf_brazo:main",
        ],
    },
)
