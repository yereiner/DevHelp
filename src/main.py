import argparse
import sys
import os

# --- CONFIGURACIÓN DE RUTAS ---
# Esto asegura que Python encuentre 'search' y 'display' aunque lances el comando 
# desde cualquier carpeta de tu terminal.
sys.path.append(os.path.dirname(__file__))

try:
    from search import buscar, listar_terminos
    from display import mostrar_resultado
except ImportError:
    # Respaldo por si se ejecuta como módulo de paquete
    from src.search import buscar, listar_terminos
    from src.display import mostrar_resultado

def main():
    # 1. Configuramos el procesador de argumentos
    parser = argparse.ArgumentParser(
        description="🚀 DevHelp - Tu tutor de Python en la terminal",
        add_help=False # Desactivamos la ayuda por defecto para personalizarla
    )
    
    # Añadimos los argumentos que el programa debe reconocer
    parser.add_argument("query", nargs="?", default=None, help="El término a buscar")
    parser.add_argument("--all", action="store_true", help="Lista todos los temas")
    parser.add_argument("-h", "--help", action="help", help="Muestra esta ayuda")

    args = parser.parse_args()

    # 2. Lógica del comando --all
    if args.all:
        terminos = listar_terminos()
        print("\n" + "="*40)
        print(" 📚 TEMAS DISPONIBLES EN TU BETA ")
        print("="*40)
        
        # Mostramos los términos en 3 columnas para que se vea profesional
        for i in range(0, len(terminos), 3):
            grupo = terminos[i:i+3]
            linea = "  ".join(f"• {t:<12}" for t in grupo)
            print(f" {linea}")
            
        print("="*40)
        print(f" Total: {len(terminos)} maestros cargados.\n")
        return

    # 3. Lógica de búsqueda normal
    if args.query:
        resultado, sugerencia = buscar("python", args.query)
        
        if resultado:
            mostrar_resultado(resultado)
        elif sugerencia:
            print(f"\n❌ No encontré '{args.query}'.")
            print(f"💡 ¿Quisiste decir: [bold]'{sugerencia}'[/bold]?")
        else:
            print(f"\n❌ El término '{args.query}' no está registrado todavía.")
            print("👉 Prueba con 'devhelp --all' para ver qué hay disponible.")
    else:
        # Si no pone nada, mostramos la ayuda básica
        parser.print_help()

if __name__ == "__main__":
    main()