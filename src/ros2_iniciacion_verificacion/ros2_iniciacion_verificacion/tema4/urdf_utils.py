"""Utilidades para localizar y parsear el URDF/XACRO del alumno.

Se asume que `tema4_practica` instala su carpeta `urdf/` como datos del
paquete (convención documentada en el README), de forma que el fichero es
localizable vía `ament_index_python` una vez el alumno ha compilado su
paquete en el mismo workspace que este verificador.
"""
import xml.etree.ElementTree as ET

from ros2_iniciacion_verificacion.verifier_base import VerifierFailure, find_package_share_file

find_share_file = find_package_share_file


def parse_urdf_file(path):
    try:
        return ET.parse(path).getroot()
    except ET.ParseError as exc:
        raise VerifierFailure(f"'{path}' no es un XML/URDF válido: {exc}")


def process_xacro_file(path, mappings=None):
    try:
        import xacro
    except ImportError:
        raise VerifierFailure("el paquete 'xacro' no está disponible en este entorno")
    try:
        doc = xacro.process_file(path, mappings=mappings or {})
    except Exception as exc:  # noqa: BLE001 - cualquier fallo de xacro es un FAIL con diagnóstico
        raise VerifierFailure(f"xacro no ha podido procesar '{path}': {exc}")
    return ET.fromstring(doc.toxml())


def find_link(root, name):
    for link in root.findall("link"):
        if link.get("name") == name:
            return link
    return None


def find_joint(root, name):
    for joint in root.findall("joint"):
        if joint.get("name") == name:
            return joint
    return None
