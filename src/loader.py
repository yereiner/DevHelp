import json
import os

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def cargar_json(ruta_relativa):
    """
    Carga un archivo JSON de forma segura.
    """
    # Si la ruta ya es absoluta, os.path.join la respetará
    ruta_completa = os.path.join(BASE_DIR, ruta_relativa)

    if not os.path.exists(ruta_completa):
        # En lugar de romper, devolvemos None para que el migrador lo ignore
        return None

    try:
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        print(f"⚠️ Error: El archivo {ruta_relativa} tiene un formato JSON inválido.")
        return None
    except Exception as e:
        print(f"⚠️ Error inesperado al cargar {ruta_relativa}: {e}")
        return None