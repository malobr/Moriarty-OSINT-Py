import json
import asyncio
import httpx
from rich.console import Console

# Instancia o console para gerenciar as cores no terminal
console = Console()

def carregar_sites():
    try:
        with open("data/sites.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        console.print("[bold red][!] Erro: Arquivo data/sites.json não encontrado.[/bold red]")
        return None

# Adicionamos o 'semaforo' como parâmetro para limitar requisições simultâneas
async def checar_site(client, dados_site, username, semaforo):
    nome_site = dados_site.get("name", "Desconhecido")
    url = dados_site["check_url"].format(username)
    
    # O 'async with semaforo' garante que no máximo X tarefas rodem este bloco ao mesmo tempo
    async with semaforo:
        try:
            # Reduzi o timeout para 5 segundos. 10s em OSINT atrasa muito o processo geral.
            response = await client.get(url, timeout=5.0)
            error_type = dados_site.get("errorType")
            
            if error_type == "status_code":
                if response.status_code == 200:
                    return f"[bold green][+] {nome_site}: Encontrado![/bold green] ({url})"
                elif response.status_code == 404:
                    return f"[dim red][-] {nome_site}: Não encontrado.[/dim red]"
                    
            elif error_type == "message":
                error_msg = dados_site.get("errorMsg", "")
                if response.status_code == 200:
                    if error_msg in response.text:
                        return f"[dim red][-] {nome_site}: Não encontrado (Falso Positivo evitado).[/dim red]"
                    else:
                        return f"[bold green][+] {nome_site}: Encontrado![/bold green] ({url})"
                        
            return f"[bold yellow][?] {nome_site}: Status inesperado ({response.status_code})[/bold yellow]"
            
        except httpx.RequestError:
            return f"[bold magenta][!] {nome_site}: Erro de conexão ou timeout.[/bold magenta]"

async def rodar_motor(username):
    dados_json = carregar_sites()
    
    if not dados_json or "sites" not in dados_json:
        console.print("[bold red][!] Erro na estrutura do sites.json[/bold red]")
        return

    lista_sites = dados_json["sites"]

    console.print(f"\n[bold cyan][*] Iniciando buscas assíncronas para o usuário:[/bold cyan] [bold white]{username}[/bold white]...\n")
    
    # Limita a 20 conexões simultâneas para não estourar os limites da máquina/rede
    semaforo = asyncio.Semaphore(20)
    
    async with httpx.AsyncClient(headers={"User-Agent": "Moriarty-OSINT/1.0"}) as client:
        tarefas = []
        
        for dados_site in lista_sites:
            if "check_url" in dados_site:
                tarefa = checar_site(client, dados_site, username, semaforo)
                tarefas.append(tarefa)
        
        resultados = await asyncio.gather(*tarefas)
        
        for resultado in resultados:
            # Usamos o console.print do 'rich' no lugar do print padrão para renderizar as tags de cor
            console.print(resultado)

if __name__ == "__main__":
    alvo = input("Digite o username para buscar: ")
    asyncio.run(rodar_motor(alvo))