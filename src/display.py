from src.search import buscar
import os

def imprimir(datos):
    if not datos:
        print("\n[!] No se encontró información para ese término.")
        return

    # Limpiar pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

    # Colores básicos (opcional, funcionan en la mayoría de terminales modernas)
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    print("=" * 60)
    print(f"{BOLD}  DOCUMENTACIÓN DE: {datos.get('name', 'N/A').upper()}{RESET}")
    print("=" * 60)

    print(f"\n📌 {BOLD}Descripción:{RESET} {datos.get('description', 'Sin descripción')}")
    print(f"💻 {BOLD}Sintaxis:{RESET} {datos.get('syntax', 'N/A')}")

    # Parámetros
    parametros = datos.get('parameters', [])
    if parametros:
        print(f"\n🔹 {BOLD}Parámetros:{RESET}")
        for p in parametros:
            opcional = "(Opcional)" if p.get('optional') else "(Requerido)"
            print(f"  - {p['name']} ({p['type']}): {p['description']} {opcional}")

    # Ejemplos
    ejemplos = datos.get('examples', [])
    if ejemplos:
        print(f"\n🚀 {BOLD}Ejemplos de uso:{RESET}")
        for ej in ejemplos:
            print(f"  # {ej['description']}")
            print(f"  {ej['code']}")
            print("-" * 20)

    # --- NUEVA SECCIÓN: ERRORES COMUNES ---
    errores = datos.get('common_errors', [])
    if errores:
        print(f"\n⚠️  {RED}{BOLD}ERRORES COMUNES:{RESET}")
        for err in errores:
            print(f"  • {BOLD}{err['error']}{RESET}: {err['reason']}")

    print("\n" + "=" * 60)
