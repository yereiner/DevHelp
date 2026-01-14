import argparse
import sys
import os

# --- LÓGICA DE RUTA DINÁMICA ---
# Buscamos la carpeta 'src/data/python/devhelp.db'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "python", "devhelp.db")

try:
    from src.search import buscar, listar_terminos
    from src.display import mostrar_resultado
except ImportError:
    from search import buscar, listar_terminos
    from display import mostrar_resultado

def main():
    parser = argparse.ArgumentParser(
        description="🚀 DevHelp - Tu tutor de Python en la terminal",
        add_help=False 
    )
    
    parser.add_argument("query", nargs="?", default=None, help="El término a buscar")
    parser.add_argument("--all", action="store_true", help="Lista todos los temas")
    parser.add_argument("-h", "--help", action="help", help="Muestra esta ayuda")

    args = parser.parse_args()

    if args.all:
        # Pasamos la ruta detectada a la función
        terminos = listar_terminos(DB_PATH) 
        print("\n" + "="*80)
        print(" 📚 TEMAS DISPONIBLES DE LA 1.0 ")
        print("="*80)
        
        if not terminos:
            print(f" ⚠️  No se encontró la base de datos en: {DB_PATH}")
        else:
            for i in range(0, len(terminos), 3):
                grupo = terminos[i:i+3]
                linea = "  ".join(f"• {t:<22}" for t in grupo)
                print(f" {linea}")
            
        print("="*80)
        print(f" Total: {len(terminos)} maestros cargados.\n")
        return

    if args.query:
        # Pasamos la ruta detectada a la función
        resultado, sugerencia = buscar("python", args.query, DB_PATH)
        
        if resultado:
            mostrar_resultado(resultado)
        elif sugerencia:
            print(f"\n❌ No encontré '{args.query}'.")
            print(f"💡 ¿Quisiste decir: '{sugerencia}'?")
        else:
            print(f"\n❌ El término '{args.query}' no está registrado.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()