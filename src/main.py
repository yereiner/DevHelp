import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# IMPORTANTE: Necesitamos importar la función buscar para que el programa funcione
from src.search import buscar, listar_terminos

console = Console()

def imprimir(datos):
    """Tu lógica visual integrada dentro de main"""
    if not datos:
        console.print("\n[bold red][!] No se encontró información para ese término.[/bold red]")
        return

    nombre = datos.get('name', 'N/A').upper()
    descripcion = datos.get('description', 'Sin descripción')
    sintaxis = datos.get('syntax', 'N/A')

    console.print(f"\n[bold cyan]🔍 DOCUMENTACIÓN: {nombre} (PYTHON)[/bold cyan]")

    info_principal = f"{descripcion}\n\n[bold yellow]Sintaxis:[/bold yellow] [green]{sintaxis}[/green]"
    console.print(Panel(info_principal, border_style="bright_blue", title="Descripción General"))

    # Parámetros
    parametros = datos.get('parameters', [])
    if parametros:
        tabla = Table(title="🔹 Parámetros", show_header=True, header_style="bold magenta")
        tabla.add_column("Nombre", style="dim")
        tabla.add_column("Tipo")
        tabla.add_column("Descripción")
        for p in parametros:
            opcional = "[dim](Opcional)[/dim]" if p.get('optional') else "[bold red](Requerido)[/bold red]"
            tabla.add_row(p['name'], p['type'], f"{p['description']} {opcional}")
        console.print(tabla)

    # Ejemplos
    ejemplos = datos.get('examples', [])
    if ejemplos:
        for ej in ejemplos:
            contenido_ej = f"[dim]# {ej['description']}[/dim]\n{ej['code']}"
            console.print(Panel(contenido_ej, title="🚀 Ejemplo de uso", border_style="green"))

    # Errores
    errores = datos.get('common_errors', [])
    if errores:
        error_text = Text()
        for err in errores:
            error_text.append(f"• {err['error']}: ", style="bold red")
            error_text.append(f"{err['reason']}\n", style="white")
        console.print(Panel(error_text, title="⚠️ ERRORES COMUNES", border_style="red"))

    console.print("=" * 60 + "\n")

# --- ESTA ES LA PARTE QUE FALTABA PARA QUE EL PROGRAMA ARRANQUE ---

def main():
    """Función que recibe el comando de la terminal"""
    if len(sys.argv) < 2:
        disponibles = listar_terminos()
        guia = ", ".join(disponibles[:5]) if disponibles else "int, print, for"
        console.print("\n[bold yellow]👋 ¡Hola! Soy DevHelp.[/bold yellow]")
        console.print(f"[dim]Prueba buscando: {guia}...[/dim]\n")
        return

    query = sys.argv[1]
    
    # Buscamos en la base de datos
    resultado, sugerencia = buscar("python", query)

    if resultado:
        imprimir(resultado) # Llamamos a la función visual de arriba
    elif sugerencia:
        console.print(f"\n[bold yellow]💡 ¿Quisiste decir '{sugerencia}'?[/bold yellow]")
        console.print(f"[dim]Ejecuta: devhelp {sugerencia}[/dim]\n")
    else:
        console.print(f"\n[bold red]❌ No se encontró '{query}'.[/bold red]\n")

if __name__ == "__main__":
    main()