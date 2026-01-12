import sqlite3
import os

# Usamos una ruta más robusta basada en la ubicación del archivo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "devhelp.db")

def init_db():
    """Crea la base de datos y la tabla preparada para documentación completa."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Expandimos la tabla para que coincida con tus archivos maestros
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS docs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            language TEXT NOT NULL,
            term TEXT NOT NULL,
            definition TEXT NOT NULL,
            syntax TEXT,
            example TEXT,
            extra_info TEXT, -- Aquí guardaremos parámetros y errores en formato JSON o texto
            UNIQUE(language, term)
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"✅ Base de datos inicializada en: {DB_PATH}")

if __name__ == "__main__":
    init_db()