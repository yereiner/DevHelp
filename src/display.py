import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.syntax import Syntax  # <--- NUEVA: Para el resaltado de colores

console = Console()

def mostrar_resultado(datos):
    if not datos:
        console.print("\n[bold red][!] No se encontró información para ese término.[/bold red]")
        return

    nombre = datos.get('name', 'N/A').upper()
    descripcion = datos.get('description', 'Sin descripción')
    sintaxis = datos.get('syntax', 'N/A')

    # Encabezado
    console.print(f"\n[bold cyan]🔍 DOCUMENTACIÓN: {nombre} (PYTHON)[/bold cyan]")

    # Panel de Información Principal
    info_principal = f"{descripcion}\n\n[bold yellow]Sintaxis:[/bold yellow] [green]{sintaxis}[/green]"
    console.print(Panel(info_principal, border_style="bright_blue", title="Descripción General"))

    # Sección de Parámetros
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

    # Sección de Ejemplos con CÓDIGO VIVO
    ejemplos = datos.get('examples', [])
    if ejemplos:
        for ej in ejemplos:
            console.print(f"\n[bold magenta]🚀 Ejemplo: {ej['description']}[/bold magenta]")
            
            # Configuramos el resaltado de sintaxis tipo VS Code
            codigo_resaltado = Syntax(
                ej['code'], 
                "python", 
                theme="monokai",       # El tema clásico de VSC
                line_numbers=True,     # Números de línea para guiar al usuario
                background_color="default"
            )
            
            console.print(Panel(codigo_resaltado, border_style="green"))

    # Sección de Errores Comunes
    errores = datos.get('common_errors', [])
    if errores:
        error_text = Text()
        for err in errores:
            error_text.append(f"• {err['error']}: ", style="bold red")
            error_text.append(f"{err['reason']}\n", style="white")
        
        console.print(Panel(error_text, title="⚠️ ERRORES COMUNES", border_style="red"))

    console.print("=" * 60 + "\n")