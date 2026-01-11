import argparse
from src.search import buscar
from src.display import imprimir

def main():
    # 1. Creamos el manejador de argumentos
    parser = argparse.ArgumentParser(
        description="DevHelp: Consulta documentación de programación desde la terminal."
    )

    # 2. Definimos qué argumentos esperamos
    # Argumentos posicionales (obligatorios en este orden)
    parser.add_argument("lenguaje", help="El lenguaje de programación (ej: python, js)")
    parser.add_argument("termino", help="El comando o función a buscar (ej: range, print)")

    # 3. Procesamos los argumentos que el usuario escribió
    args = parser.parse_args()

    # 4. Usamos los datos
    print(f"🔍 Buscando '{args.termino}' en {args.lenguaje}...")
    
    resultado = buscar(args.lenguaje, args.termino)
    imprimir(resultado)

if __name__ == "__main__":
    main()