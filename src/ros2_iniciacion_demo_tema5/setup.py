from glob import glob
from setuptools import setup, find_packages

package_name = "ros2_iniciacion_demo_tema5"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name + "/launch", glob("launch/*.launch.py")),
        ("share/" + package_name + "/config", glob("config/*")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Francisco José Mañas Álvarez",
    maintainer_email="fma527@ual.es",
    description="Demo de RViz/RQT, PyQt y foxglove_bridge (Tema 5)",
    license="MIT",
    entry_points={
        "console_scripts": [
            "nodo_gui_pyqt_demo = ros2_iniciacion_demo_tema5.nodo_gui_pyqt_demo:main",
        ],
    },
)
