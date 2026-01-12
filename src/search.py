import os
import sqlite3
import difflib

# Ruta a la base de datos (subiendo desde src/ a la raíz)
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "devhelp.db")

def buscar(lenguaje, termino):
    """
    Busca un término en la base de datos. 
    Retorna (datos, sugerencia)
    """
    termino = termino.lower().strip()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Intento de búsqueda exacta
    cursor.execute("SELECT term, definition, example FROM docs WHERE term = ?", (termino,))
    resultado = cursor.fetchone()

    if resultado:
        conn.close()
        # Retornamos los datos en el formato que espera tu display.py
        return {
            "name": resultado[0],
            "description": resultado[1],
            "examples": [{"code": resultado[2]}]
        }, None

    # 2. Si no hay éxito, buscamos la palabra más parecida (Sugerencia)
    cursor.execute("SELECT term FROM docs")
    todos_los_terminos = [fila[0] for fila in cursor.fetchall()]
    conn.close()

    # Buscamos la coincidencia más cercana (60% de similitud mínima)
    coincidencias = difflib.get_close_matches(termino, todos_los_terminos, n=1, cutoff=0.6)
    
    sugerencia = coincidencias[0] if coincidencias else None
    return None, sugerencia

def listar_terminos(lenguaje=None):
    """Devuelve todos los términos guardados en la DB"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT term FROM docs")
    terminos = [fila[0] for fila in cursor.fetchall()]
    conn.close()
    return sorted(terminos)