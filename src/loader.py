import json
import os

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def cargar_json(ruta_relativa):
    """
    Carga un archivo JSON y devuelve su contenido como diccionario.
    
    :param ruta_relativa: Ruta relativa desde la raíz del proyecto
    :return: dict con la información del JSON
    """
    ruta_completa = os.path.join(BASE_DIR, ruta_relativa)

    with open(ruta_completa, "r", encoding="utf-8") as archivo:
        informacion = json.load(archivo)

    return informacion
