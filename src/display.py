from src.search import buscar
import os

def imprimir(datos):
    if not datos:
        print("\n[!] No se encontró información para ese término.")
        return

    # Limpiar la terminal para una mejor experiencia visual
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 50)
    print(f"  DOCUMENTACIÓN: {datos.get('name', 'N/A').upper()}")
    print("=" * 50)

    # Descripción general
    print(f"\n📌 Descripción: {datos.get('description', 'Sin descripción')}")
    print(f"💻 Sintaxis: {datos.get('syntax', 'N/A')}")

    # Parámetros
    parametros = datos.get('parameters', [])
    if parametros:
        print("\n🔹 Parámetros:")
        for p in parametros:
            opcional = "(Opcional)" if p.get('optional') else "(Requerido)"
            print(f"  - {p['name']} ({p['type']}): {p['description']} {opcional}")

    # Ejemplos
    ejemplos = datos.get('examples', [])
    if ejemplos:
        print("\n🚀 Ejemplos de uso:")
        for ej in ejemplos:
            print(f"  # {ej['description']}")
            print(f"  {ej['code']}")
            print("-" * 20)

    print("\n" + "=" * 50)