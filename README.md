# Moriarty

**Moriarty** é um framework de OSINT (Open Source Intelligence) rápido e assíncrono, desenvolvido em Python. Seu foco principal é o reconhecimento automatizado e a enumeração de usuários em dezenas de plataformas simultaneamente, utilizando concorrência para alta performance.

## Funcionalidades

* **Motor Assíncrono:** Construído com `asyncio` e `httpx`, permitindo disparar centenas de requisições simultâneas sem bloquear o processamento (I/O Bound otimizado).
* **Prevenção de Falsos Positivos:** Sistema inteligente de validação de respostas que não depende apenas de *Status Codes* (HTTP 404), mas também analisa o conteúdo HTML em busca de strings de erro específicas.
* **Interface CLI Robusta:** Utiliza `argparse` para uma linha de comando nativa e rápida, e `Rich` para saídas visuais elegantes e fáceis de ler no terminal.
* **Arquitetura Escalável:** Base de alvos centralizada em um arquivo JSON (`sites.json`), facilitando a adição de novos sites sem precisar alterar o código do motor.

---

## Estrutura do Projeto

```text
moriarty/
├── data/
│   └── sites.json          # Banco de dados de alvos e regras de validação
├── src/
│   ├── __init__.py
│   ├── main.py             # Interface CLI (Roteamento de argumentos)
│   └── motor.py            # Core assíncrono e lógica de requisições HTTP
├── requirements.txt        # Dependências do projeto
├── setup.py                # OBRIGATÓRIO: Configuração do pacote e binário CLI
└── README.md               # Documentação

```

---

## Instalação

Para baixar e instalar o pacote Moriarty diretamente, execute o comando abaixo no seu terminal.

> **Nota para usuários Linux:** É recomendado utilizar um ambiente virtual (`venv`) ou o `pipx` para evitar conflitos com pacotes do sistema.

**Pré-requisitos:** Python 3.8+ e Git (apenas se for instalar via protocolo Git).

**Opção 1 (Recomendada - Requer Git):**
```
pip install git+https://github.com/SeuUsuario/Moriarty-OSINT-Py.git
```
**Opção 2 (Não requer Git):**
```
pip install https://github.com/SeuUsuario/Moriarty-OSINT-Py/archive/refs/heads/main.zip
```


## Como Usar

Após a instalação, o Moriarty estará disponível como um comando nativo no seu terminal. Basta digitar:

```bash
# Para ver o menu de ajuda e todas as opções:
moriarty --help

# Para buscar um nome de usuário em todas as plataformas:
moriarty -u alvo123

```

---

## Como adicionar novos sites (Configuração)

Para ensinar o Moriarty a buscar em um novo site, basta adicionar um novo bloco ao arquivo `data/sites.json`. Você tem duas abordagens principais:

**1. Validação Simples (Por Status Code):**
Usado quando o site respeita os padrões HTTP e retorna um erro 404 genuíno se o perfil não existir.

```json
{
  "name": "GitHub",
  "check_url": "[https://github.com/](https://github.com/){}",
  "errorType": "status_code"
}

```

**2. Validação Avançada (Por String no HTML):**
Usado para evitar **Falsos Positivos** quando o site retorna Status 200 OK, mas exibe uma página de erro personalizada ou texto avisando que a conta não existe.

```json
{
  "name": "Instagram",
  "check_url": "[https://www.instagram.com/](https://www.instagram.com/){}/",
  "errorType": "message",
  "errorMsg": "Esta página não está disponível"
}

```

*(Nota: Certifique-se de que a chave `{}` esteja presente na `check_url` para que o Moriarty possa injetar automaticamente o nome de usuário procurado).*

---

## Aviso Legal

O **Moriarty** foi desenvolvido com propósitos puramente educacionais e para auxiliar analistas de inteligência e pesquisadores de segurança. O uso desta ferramenta para coletar dados de forma massiva pode violar os Termos de Serviço de algumas plataformas. Use com responsabilidade e ética.

