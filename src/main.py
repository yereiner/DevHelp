import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# Importamos la lógica de búsqueda
from src.search import buscar, listar_terminos

console = Console()

def imprimir(datos):
    """Muestra la información con manejo seguro de llaves (evita KeyError)."""
    if not datos:
        console.print("\n[bold red][!] No se encontró información para ese término.[/bold red]")
        return

    # Extraemos datos básicos con valores por defecto
    nombre = datos.get('name', 'N/A').upper()
    descripcion = datos.get('description', 'Sin descripción disponible.')
    sintaxis = datos.get('syntax', 'No especificada.')

    console.print(f"\n[bold cyan]🔍 DOCUMENTACIÓN: {nombre} (PYTHON)[/bold cyan]")

    # Panel principal
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
            # Uso de .get para evitar errores si falta una columna en el JSON
            nombre_p = p.get('name', '?')
            tipo_p = p.get('type', 'Dato')
            desc_p = p.get('description', '-')
            opcional = "[dim](Opcional)[/dim]" if p.get('optional') else "[bold red](Requerido)[/bold red]"
            tabla.add_row(nombre_p, tipo_p, f"{desc_p} {opcional}")
        console.print(tabla)

    # Sección de Ejemplos - AQUÍ ESTABA EL ERROR
    ejemplos = datos.get('examples', [])
    if ejemplos:
        for ej in ejemplos:
            # CAMBIO CLAVE: Usamos .get() en lugar de corchetes directos
            desc_ej = ej.get('description', 'Ejemplo de uso')
            code_ej = ej.get('code', '# Sin código disponible')
            
            contenido_ej = f"[dim]# {desc_ej}[/dim]\n{code_ej}"
            console.print(Panel(contenido_ej, title="🚀 Ejemplo", border_style="green"))

    # Sección de Errores Comunes
    errores = datos.get('common_errors', [])
    if errores:
        error_text = Text()
        for err in errores:
            e_name = err.get('error', 'Error')
            e_reason = err.get('reason', 'Sin motivo especificado')
            error_text.append(f"• {e_name}: ", style="bold red")
            error_text.append(f"{e_reason}\n", style="white")
        
        console.print(Panel(error_text, title="⚠️ ERRORES COMUNES", border_style="red"))

    console.print("=" * 60 + "\n")

def main():
    if len(sys.argv) < 2:
        disponibles = listar_terminos()
        ejemplos_guia = ", ".join(disponibles[:5]) if disponibles else "int, print, for"
        console.print("\n[bold yellow]👋 ¡Hola! Soy DevHelp.[/bold yellow]")
        console.print(f"[dim]Prueba buscando: {ejemplos_guia}...[/dim]\n")
        return

    query = sys.argv[1]
    resultado, sugerencia = buscar("python", query)

    if resultado:
        imprimir(resultado)
    elif sugerencia:
        console.print(f"\n[bold yellow]💡 ¿Quisiste decir '{sugerencia}'?[/bold yellow]")
        console.print(f"[dim]Ejecuta: devhelp {sugerencia}[/dim]\n")
    else:
        console.print(f"\n[bold red]❌ No se encontró '{query}'.[/bold red]\n")

if __name__ == "__main__":
    main()