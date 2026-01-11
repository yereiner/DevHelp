
# src/main.py
from src.search import buscar
from src.display import imprimir

def main():
    # Simulamos que el usuario pidió documentación de "range" en "python"
    lenguaje = "python"
    termino = "range"
    
    print(f"🔍 Buscando '{termino}' en {lenguaje}...")
    
    # 1. Buscamos los datos (esto usa search.py)
    resultado = buscar(lenguaje, termino)
    
    # 2. Imprimimos los datos 
    imprimir(resultado)

if __name__ == "__main__":
    main()