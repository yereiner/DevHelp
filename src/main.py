# src/main.py
from src.search import buscar
from src.display import imprimir

def main():
    print("--- Bienvenido a DevHelp CLI ---")
    
    # Pedimos los datos al usuario
    lenguaje = input("¿Qué lenguaje quieres consultar? (ej. python): ").strip()
    termino = input(f"¿Qué término de {lenguaje} buscas? (ej. range): ").strip()
    
    if not lenguaje or not termino:
        print("Error: Debes ingresar tanto el lenguaje como el término.")
        return

    print(f"\n🔍 Buscando '{termino}' en {lenguaje}...")
    
    # Buscamos y mostramos
    resultado = buscar(lenguaje, termino)
    imprimir(resultado)

if __name__ == "__main__":
    main()