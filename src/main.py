import argparse
import sys
import os

# --- IMPORTACIONES ABSOLUTAS ---
# Al instalarse como paquete, Python necesita el prefijo 'src.' 
# para localizar los módulos correctamente.
from src.search import buscar, listar_terminos
from src.display import mostrar_resultado

def main():
    # 1. Configuración del procesador de argumentos
    parser = argparse.ArgumentParser(
        description="🚀 DevHelp - Tu tutor de Python en la terminal",
        add_help=False 
    )
    
    # Definición de comandos y flags
    parser.add_argument("query", nargs="?", default=None, help="El término a buscar")
    parser.add_argument("--all", action="store_true", help="Lista todos los temas")
    parser.add_argument("-h", "--help", action="help", help="Muestra esta ayuda")

    args = parser.parse_args()

    # 2. Lógica para listar todos los temas disponibles (--all)
    if args.all:
        terminos = listar_terminos()
        print("\n" + "="*40)
        print(" 📚 TEMAS DISPONIBLES EN TU BETA ")
        print("="*40)
        
        # Mostramos los términos organizados en 3 columnas
        for i in range(0, len(terminos), 3):
            grupo = terminos[i:i+3]
            linea = "  ".join(f"• {t:<12}" for t in grupo)
            print(f" {linea}")
            
        print("="*40)
        print(f" Total: {len(terminos)} maestros cargados.\n")
        return

    # 3. Lógica de búsqueda principal
    if args.query:
        # Buscamos en la categoría 'python' (puedes ampliarlo luego)
        resultado, sugerencia = buscar("python", args.query)
        
        if resultado:
            # Si hay éxito, 'display' se encarga de la magia visual con Rich
            mostrar_resultado(resultado)
        elif sugerencia:
            # Si no hay match exacto, ofrecemos la alternativa más cercana
            print(f"\n❌ No encontré '{args.query}'.")
            print(f"💡 ¿Quisiste decir: '{sugerencia}'?")
        else:
            # Si el término es totalmente desconocido
            print(f"\n❌ El término '{args.query}' no está registrado todavía.")
            print("👉 Prueba con 'devhelp --all' para ver qué hay disponible.")
    else:
        # Si el usuario ejecuta 'devhelp' solo, mostramos la ayuda
        parser.print_help()

if __name__ == "__main__":
    main()