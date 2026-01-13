import os
import sqlite3
import difflib
import json

# Ruta a la base de datos (subiendo desde src/ a la raíz del proyecto)
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "devhelp.db")

def buscar(lenguaje, termino):
    """
    Busca un término en la base de datos con soporte para sintaxis y pedagogía. 
    Retorna (datos, sugerencia)
    """
    termino = termino.lower().strip()
    
    # Conexión segura a la base de datos
    conn = sqlite3.connect(DB_PATH)
    # Permite acceder a las columnas por nombre (fila['term'])
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()

    # 1. Búsqueda exacta
    cursor.execute("""
        SELECT term, definition, syntax, parameters, examples, common_errors 
        FROM docs WHERE term = ?
    """, (termino,))
    
    fila = cursor.fetchone()

    if fila:
        conn.close()
        # Convertimos la fila en un diccionario real
        res = dict(fila)
        
        # Retornamos el diccionario procesando los campos JSON
        return {
            "name": res["term"],
            "description": res["definition"],
            "syntax": res["syntax"],
            "parameters": json.loads(res["parameters"]) if res["parameters"] else [],
            "examples": json.loads(res["examples"]) if res["examples"] else [],
            "common_errors": json.loads(res["common_errors"]) if res["common_errors"] else []
        }, None

    # 2. Si no hay éxito, buscamos sugerencias con difflib
    cursor.execute("SELECT term FROM docs")
    todos_los_terminos = [f[0] for f in cursor.fetchall()]
    conn.close()

    coincidencias = difflib.get_close_matches(termino, todos_los_terminos, n=1, cutoff=0.6)
    sugerencia = coincidencias[0] if coincidencias else None
    
    return None, sugerencia

def listar_terminos():
    """Devuelve todos los términos guardados ordenados alfabéticamente"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT term FROM docs")
        terminos = [fila[0] for fila in cursor.fetchall()]
        conn.close()
        return sorted(terminos)
    except Exception as e:
        print(f"Error al listar términos: {e}")
        return []