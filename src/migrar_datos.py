import json
import sqlite3
import os

# Usamos rutas relativas robustas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "devhelp.db")
RUA_PYTHON = os.path.join(BASE_DIR, "src", "data", "python")

def migrar():
    if not os.path.exists(RUA_PYTHON):
        print(f"⚠️ No se encontró la carpeta: {RUA_PYTHON}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Limpiamos para una carga limpia
    cursor.execute("DELETE FROM docs")

    archivos = [f for f in os.listdir(RUA_PYTHON) if f.endswith('.json')]
    
    for nombre_archivo in archivos:
        ruta_completa = os.path.join(RUA_PYTHON, nombre_archivo)
        
        try:
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                
                # Manejamos si el JSON es una lista de objetos o un objeto único
                lista_elementos = datos if isinstance(datos, list) else [datos]

                for item in lista_elementos:
                    termino = item.get('name', '').lower().strip()
                    if not termino: continue

                    # Extraemos campos pedagógicos
                    definic = item.get('description', "Sin descripción")
                    sintaxis = item.get('syntax', "N/A")
                    
                    # Convertimos listas complejas (parámetros/errores) a JSON string 
                    # para que search.py pueda recuperarlos fácilmente
                    ejemplos = item.get('examples', [])
                    ejem_codigo = ejemplos[0].get('code', "") if ejemplos else ""
                    
                    # Guardamos TODO en la base de datos expandida
                    cursor.execute('''
                        INSERT OR REPLACE INTO docs (language, term, definition, syntax, example)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (item.get('language', 'Python'), termino, definic, sintaxis, ejem_codigo))
        
        except Exception as e:
            print(f"❌ Error procesando {nombre_archivo}: {e}")

    conn.commit()
    conn.close()
    print(f"🚀 ¡Migración exitosa! {len(archivos)} archivos maestros procesados en {DB_PATH}")

if __name__ == "__main__":
    migrar()