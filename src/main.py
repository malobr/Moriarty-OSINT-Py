import argparse
import asyncio
from rich.console import Console
from src.motor import rodar_motor  # Importa a lógica que construímos no motor.py

console = Console()

def mostrar_banner():
    banner = """
    [bold red]
    ███╗   ███╗ ██████╗ ██████╗ ██╗ █████╗ ██████╗ ████████╗██╗   ██╗
    ████╗ ████║██╔═══██╗██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝╚██╗ ██╔╝
    ██╔████╔██║██║   ██║██████╔╝██║███████║██████╔╝   ██║    ╚████╔╝ 
    ██║╚██╔╝██║██║   ██║██╔══██╗██║██╔══██║██╔══██╗   ██║     ╚██╔╝  
    ██║ ╚═╝ ██║╚██████╔╝██║  ██║██║██║  ██║██║  ██║   ██║      ██║   
    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   
    [/bold red]
    [bold white]OSINT Framework - v1.0[/bold white]
    """
    console.print(banner)

def main():
    # Configura o menu de ajuda (--help)
    parser = argparse.ArgumentParser(
        description="Moriarty - Framework de OSINT para busca de informações em fontes abertas.",
        epilog="Exemplo de uso: moriarty -u marcelo -e alvo@email.com"
    )

    # Definindo as opções da linha de comando
    parser.add_argument("-u", "--username", help="Busca por nome de usuário (ex: -u alvo123)", type=str)
    parser.add_argument("-e", "--email", help="Busca informações relacionadas a um endereço de e-mail", type=str)
    parser.add_argument("-p", "--phone", help="Busca informações atreladas a um número de telefone", type=str)

    # Lê o que o usuário digitou no terminal
    args = parser.parse_args()

    # Mostra a arte ASCII
    mostrar_banner()

    # Roteador: Decide o que fazer baseado no argumento passado
    if getattr(args, 'username'):
        console.print(f"[bold cyan][*] Iniciando módulo de Username para:[/bold cyan] {args.username}")
        # Chama o motor.py passando o alvo
        asyncio.run(rodar_motor(args.username))
        
    elif getattr(args, 'email'):
        # Aqui você futuramente conectará um 'motor_email.py'
        console.print(f"[bold yellow][*] Módulo de E-mail em desenvolvimento. Alvo selecionado:[/bold yellow] {args.email}")
        
    elif getattr(args, 'phone'):
        # Aqui você futuramente conectará um 'motor_telefone.py'
        console.print(f"[bold yellow][*] Módulo de Telefone em desenvolvimento. Alvo selecionado:[/bold yellow] {args.phone}")
        
    else:
        # Se o usuário digitar só "moriarty" sem argumentos
        console.print("[bold red][!] Nenhum alvo fornecido. Use 'moriarty --help' para ver as opções disponíveis.[/bold red]")

if __name__ == "__main__":
    main()
