import json
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "devhelp.db")
RUA_PYTHON = os.path.join(BASE_DIR, "src", "data", "python")

def migrar():
    if not os.path.exists(RUA_PYTHON):
        print(f"⚠️ No se encontró la carpeta: {RUA_PYTHON}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM docs")

    archivos = [f for f in os.listdir(RUA_PYTHON) if f.endswith('.json')]
    
    for nombre_archivo in archivos:
        ruta_completa = os.path.join(RUA_PYTHON, nombre_archivo)
        try:
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                lista_elementos = datos if isinstance(datos, list) else [datos]

                for item in lista_elementos:
                    termino = item.get('name', '').lower().strip()
                    if not termino: continue

                    # Guardamos los objetos complejos como texto (JSON string) 
                    # para que main.py pueda leerlos con .get()
                    cursor.execute('''
                        INSERT OR REPLACE INTO docs 
                        (language, term, definition, syntax, parameters, examples, common_errors)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        item.get('language', 'Python'),
                        termino,
                        item.get('description', "Sin descripción"),
                        item.get('syntax', "No especificada."),
                        json.dumps(item.get('parameters', [])),
                        json.dumps(item.get('examples', [])),
                        json.dumps(item.get('common_errors', []))
                    ))
        except Exception as e:
            print(f"❌ Error procesando {nombre_archivo}: {e}")

    conn.commit()
    conn.close()
    print(f"🚀 ¡Migración exitosa! {len(archivos)} maestros cargados.")

if __name__ == "__main__":
    migrar()