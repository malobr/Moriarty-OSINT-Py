import sys
import argparse
import asyncio
from rich.console import Console
from rich.table import Table

# Importando a função do motor
from src.motor import rodar_motor

console = Console()

BANNER = """[bold red]
    ███╗   ███╗ ██████╗ ██████╗ ██╗ █████╗ ██████╗ ████████╗██╗   ██╗
    ████╗ ████║██╔═══██╗██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝╚██╗ ██╔╝
    ██╔████╔██║██║   ██║██████╔╝██║███████║██████╔╝   ██║    ╚████╔╝
    ██║╚██╔╝██║██║   ██║██╔══██╗██║██╔══██║██╔══██╗   ██║     ╚██╔╝
    ██║ ╚═╝ ██║╚██████╔╝██║  ██║██║██║  ██║██║  ██║   ██║      ██║
    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝
[/bold red]"""

def mostrar_ajuda_customizada():
    console.print(BANNER)
    console.print("    [bold cyan]OSINT Framework - v1.0[/bold cyan]\n")
    
    tabela = Table(show_header=True, header_style="bold magenta", border_style="dim")
    tabela.add_column("Argumento", style="cyan", width=25)
    tabela.add_column("Descrição", style="white")
    
    tabela.add_row("-h, --help", "Mostra este menu de ajuda customizado")
    tabela.add_row("-u, --username", "Busca por nome de usuário (ex: -u alvo123)")
    tabela.add_row("-e, --email", "Busca informações de um endereço de e-mail")
    tabela.add_row("-p, --phone", "Busca informações atreladas a um número de telefone")
    
    console.print(tabela)
    console.print("\n[dim]Exemplo de uso: moriarty -u marcelo -e alvo@email.com[/dim]\n")

def main():
    # 1. Menu de ajuda customizado
    if "-h" in sys.argv or "--help" in sys.argv or len(sys.argv) == 1:
        mostrar_ajuda_customizada()
        sys.exit(0)

    # 2. Configura os argumentos
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-u", "--username")
    parser.add_argument("-e", "--email")
    parser.add_argument("-p", "--phone")
    
    args = parser.parse_args()

    # 3. Imprime a arte antes de iniciar o processo de busca
    console.print(BANNER)
    console.print("    [bold cyan]OSINT Framework - v1.0[/bold cyan]\n")

    # 4. Aciona o motor dependendo do argumento passado
    if args.username:
        asyncio.run(rodar_motor(args.username))
    elif args.email:
        console.print("[bold yellow][!] Módulo de busca por email em construção...[/bold yellow]")
    elif args.phone:
        console.print("[bold yellow][!] Módulo de busca por telefone em construção...[/bold yellow]")

if __name__ == "__main__":
    main()
