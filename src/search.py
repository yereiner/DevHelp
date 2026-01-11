# En src/search.py
import os
from src.loader import cargar_json

def buscar(lenguaje, termino):
    lenguaje = lenguaje.lower()
    termino = termino.lower()

    # --- CAMBIO CLAVE AQUÍ ---
    # 1. Obtenemos la ruta donde vive ESTE archivo (search.py)
    base_dir = os.path.dirname(__file__) 
    
    # 2. Construimos la ruta dinámica hacia la carpeta data
    ruta_relativa = os.path.join(base_dir, "data", lenguaje, f"{termino}.json")
    # -------------------------

    try:
        datos = cargar_json(ruta_relativa)
        return datos
    except FileNotFoundError:
        return None
