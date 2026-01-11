import os
from src.loader import cargar_json

def buscar(lenguaje, termino):
    lenguaje = lenguaje.lower()
    termino = termino.lower()

    # Obtenemos la ruta donde vive este archivo para que sea escalable
    base_dir = os.path.dirname(__file__) 
    
    # Construimos la ruta hacia la carpeta data
    ruta_relativa = os.path.join(base_dir, "data", lenguaje, f"{termino}.json")

    try:
        datos = cargar_json(ruta_relativa)
        return datos
    except FileNotFoundError:
        return None

def listar_terminos(lenguaje):
    """
    Escanea la carpeta del lenguaje y devuelve los nombres de los archivos JSON.
    Esto permite que el programa le diga al usuario qué puede buscar.
    """
    base_dir = os.path.dirname(__file__)
    # Buscamos en src/data/<lenguaje>
    ruta_lenguaje = os.path.join(base_dir, "data", lenguaje.lower())
    
    # Verificamos si la carpeta del lenguaje existe
    if not os.path.exists(ruta_lenguaje):
        return []
    
    # Listamos archivos .json y les quitamos la extensión .json para mostrarlos
    archivos = [f.replace('.json', '') for f in os.listdir(ruta_lenguaje) if f.endswith('.json')]
    return sorted(archivos)

def listar_lenguajes():
    """
    Devuelve una lista de todas las carpetas dentro de 'data'.
    Útil para el saludo inicial del programa.
    """
    base_dir = os.path.dirname(__file__)
    ruta_data = os.path.join(base_dir, "data")
    
    if not os.path.exists(ruta_data):
        return []
        
    # Listamos solo los directorios dentro de data/
    return [d for d in os.listdir(ruta_data) if os.path.isdir(os.path.join(ruta_data, d))]