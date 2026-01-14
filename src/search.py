import os
import sqlite3
import difflib
import json

def buscar(lenguaje, termino, db_path):
    """
    Busca un término en la base de datos.
    Retorna (datos, sugerencia)
    """
    termino = termino.lower().strip()
    
    try:
        # Usamos db_path que viene desde main.py
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()

        # 1. Búsqueda exacta
        cursor.execute("""
            SELECT term, definition, syntax, parameters, examples, common_errors 
            FROM docs WHERE term = ?
        """, (termino,))
        
        fila = cursor.fetchone()

        if fila:
            res = dict(fila)
            conn.close()
            
            return {
                "name": res["term"],
                "description": res["definition"],
                "syntax": res["syntax"],
                "parameters": json.loads(res["parameters"]) if res["parameters"] else [],
                "examples": json.loads(res["examples"]) if res["examples"] else [],
                "common_errors": json.loads(res["common_errors"]) if res["common_errors"] else []
            }, None

        # 2. Sugerencias si no hay match
        cursor.execute("SELECT term FROM docs")
        todos_los_terminos = [f[0] for f in cursor.fetchall()]
        conn.close()

        coincidencias = difflib.get_close_matches(termino, todos_los_terminos, n=1, cutoff=0.6)
        sugerencia = coincidencias[0] if coincidencias else None
        
        return None, sugerencia
    except Exception as e:
        print(f"Error en la base de datos: {e}")
        return None, None

def listar_terminos(db_path):
    """Devuelve todos los términos guardados ordenados alfabéticamente"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT term FROM docs")
        terminos = [fila[0] for fila in cursor.fetchall()]
        conn.close()
        return sorted(terminos)
    except Exception as e:
        print(f"Error al listar términos: {e}")
        return []