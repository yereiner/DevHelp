from src.loader import cargar_json 
import os 

def buscar(lenguaje, termino):

    lenguaje = lenguaje.lower()
    termino = termino.lower()

    ruta_relativa = os.path.join(
        "data",
        lenguaje,
        f"{termino}.json"
    )

    try:
        datos = cargar_json(ruta_relativa)
        return datos
    except FileNotFoundError:
        return None


