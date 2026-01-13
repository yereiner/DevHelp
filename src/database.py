import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "devhelp.db")

def crear_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Creamos la tabla con TODAS las columnas necesarias para la pedagogía
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS docs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            language TEXT,
            term TEXT UNIQUE,
            definition TEXT,
            syntax TEXT,
            parameters TEXT,
            examples TEXT,
            common_errors TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Base de datos preparada para la Beta.")

if __name__ == "__main__":
    crear_db()