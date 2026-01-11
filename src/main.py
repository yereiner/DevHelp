import argparse
import sys
from src.search import buscar, listar_terminos
from src.display import imprimir

def menu_interactivo():
    print("\n" + "="*40)
    print("🚀 BIENVENIDO A DEVHELP INTERACTIVO")
    print("   Escribe 'salir' para finalizar")
    print("="*40)

    # 1. Detectar lenguajes disponibles automáticamente
    # Esto asume que tienes carpetas en src/data/
    
    while True:
        print("\n--- Nueva Consulta ---")
        lenguaje = input("¿Qué lenguaje quieres consultar? (o 'salir'): ").strip().lower()
        
        if lenguaje == 'salir':
            print("¡Hasta luego, bro!")
            break

        # Opción para listar si el usuario no sabe qué hay
        opcion = input(f"¿Buscas un término específico o quieres ver la lista? (escribe el término o '--list'): ").strip().lower()

        if opcion == '--list':
            terminos = listar_terminos(lenguaje)
            if terminos:
                print(f"\n📚 Disponibles en {lenguaje.upper()}: {', '.join(terminos)}")
            else:
                print(f"\n[!] No hay datos para el lenguaje: {lenguaje}")
            continue
        
        if lenguaje and opcion:
            resultado = buscar(lenguaje, opcion)
            imprimir(resultado)
        else:
            print("[!] Por favor, completa los datos.")

def main():
    # Mantenemos argparse por si alguien quiere usarlo de la forma rápida (una sola consulta)
    parser = argparse.ArgumentParser(description="DevHelp CLI")
    parser.add_argument("lenguaje", nargs="?", help="Lenguaje a consultar")
    parser.add_argument("termino", nargs="?", help="Término a buscar")
    
    args = parser.parse_args()

    # Si el usuario NO pasa argumentos, entra al modo interactivo
    if args.lenguaje is None:
        menu_interactivo()
    else:
        # Si PASA argumentos, funciona como antes (una sola ejecución)
        resultado = buscar(args.lenguaje, args.termino)
        imprimir(resultado)

if __name__ == "__main__":
    main()