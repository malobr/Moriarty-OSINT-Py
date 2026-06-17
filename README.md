# Moriarty

**Moriarty** é um framework de OSINT (Open Source Intelligence) rápido e assíncrono, desenvolvido em Python. Seu foco principal é o reconhecimento automatizado e a enumeração de usuários em dezenas de plataformas simultaneamente, utilizando concorrência para alta performance.


## Funcionalidades

* **Motor Assíncrono:** Construído com `asyncio` e `httpx`, permitindo disparar centenas de requisições simultâneas sem bloquear o processamento (I/O Bound otimizado).
* **Prevenção de Falsos Positivos:** Sistema inteligente de validação de respostas que não depende apenas de *Status Codes* (HTTP 404), mas também analisa o conteúdo HTML em busca de strings de erro específicas.
* **Interface CLI Moderna:** Utiliza `Typer` para uma linha de comando robusta e `Rich` para saídas visuais elegantes e fáceis de ler no terminal.
* **Arquitetura Escalável:** Base de alvos centralizada em um arquivo JSON (`sites.json`), facilitando a adição de novos sites sem precisar alterar o código do motor.

---

## Estrutura do Projeto

\`\`\`text
moriarty/
├── data/
│   └── sites.json          # Banco de dados de alvos e regras de validação
├── src/
│   ├── __init__.py
│   ├── main.py             # Interface CLI (Typer + Rich)
│   └── motor.py            # Core assíncrono e lógica de requisições
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação
\`\`\`

---

## 🛠️ Instalação

**Pré-requisitos:** Python 3.8 ou superior.

1. Clone ou baixe este repositório.
2. Navegue até a pasta raiz do projeto:
   \`\`\`bash
   cd moriarty
   \`\`\`
3. Crie e ative um ambiente virtual:
   \`\`\`bash
   python -m venv venv
   
   # No Windows:
   venv\Scripts\activate
   # No Linux/MacOS:
   source venv/bin/activate
   \`\`\`
4. Instale as dependências:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

---

## Como Usar

O Moriarty opera via linha de comando (CLI). Para iniciar uma busca por um nome de usuário, rode o script `main.py` com o comando `search`:

\`\`\`bash
python src/main.py search "nome_do_usuario"
\`\`\`

Para ver o menu de ajuda e todos os comandos disponíveis:
\`\`\`bash
python src/main.py --help
\`\`\`

---

## Como adicionar novos sites (Configuração)

Para ensinar o Moriarty a buscar em um novo site, basta editar o arquivo `data/sites.json`. Você tem duas abordagens:

**1. Validação Simples (Por Status Code 404):**
Usado quando o site respeita os padrões HTTP e retorna um erro 404 genuíno se o perfil não existir.
\`\`\`json
"GitHub": {
  "url": "https://github.com/{}",
  "error_type": "status_code"
}
\`\`\`

**2. Validação Avançada (Por String no HTML):**
Usado para evitar **Falsos Positivos** quando o site retorna Status 200 OK, mas exibe uma página de erro personalizada.
\`\`\`json
"Instagram": {
  "url": "https://www.instagram.com/{}/",
  "error_type": "string",
  "error_string": "Esta página não está disponível"
}
\`\`\`
*(Nota: Certifique-se de que `{}` esteja presente na URL para que o Moriarty possa injetar o nome de usuário procurado).*

---

## Aviso Legal

O **Moriarty** foi desenvolvido com propósitos puramente educacionais e para auxiliar analistas de inteligência e pesquisadores de segurança. O uso desta ferramenta para coletar dados de forma massiva pode violar os Termos de Serviço de algumas plataformas. Use com responsabilidade e ética.
