import sys
import argparse
from rich.console import Console
from rich.table import Table

console = Console()

# Sua arte ASCII guardada em uma variável (note a tag de cor do rich no começo e fim)
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
    
    # Cria uma tabela elegante com o Rich
    tabela = Table(show_header=True, header_style="bold magenta", border_style="dim")
    tabela.add_column("Argumento", style="cyan", width=25)
    tabela.add_column("Descrição", style="white")
    
    # Adiciona as linhas da tabela
    tabela.add_row("-h, --help", "Mostra este menu de ajuda customizado")
    tabela.add_row("-u, --username", "Busca por nome de usuário (ex: -u alvo123)")
    tabela.add_row("-e, --email", "Busca informações de um endereço de e-mail")
    tabela.add_row("-p, --phone", "Busca informações atreladas a um número de telefone")
    
    console.print(tabela)
    console.print("\n[dim]Exemplo de uso: moriarty -u marcelo -e alvo@email.com[/dim]\n")

def main():
    # 1. INTERCEPTA O HELP ANTES DO ARGPARSE
    if "-h" in sys.argv or "--help" in sys.argv or len(sys.argv) == 1:
        mostrar_ajuda_customizada()
        sys.exit(0)

    # 2. CONFIGURA O ARGPARSE DESLIGANDO O HELP PADRÃO (add_help=False)
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-u", "--username")
    parser.add_argument("-e", "--email")
    parser.add_argument("-p", "--phone")
    
    args = parser.parse_args()

    # ... AQUI CONTINUA A SUA LÓGICA DE CHAMAR O motor.py PASSANDO OS ARGS ...
    # if args.username:
    #     asyncio.run(rodar_motor(args.username))

if __name__ == "__main__":
    main()
