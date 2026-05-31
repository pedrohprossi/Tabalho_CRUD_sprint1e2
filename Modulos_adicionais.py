from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box

# Console global compartilhado por todos os módulos
console = Console()


# ─────────────────────────────────────────────
#  HELPERS VISUAIS CENTRALIZADOS
# ─────────────────────────────────────────────

def imprimir_titulo(texto: str):
                    #Painel centralizado para títulos de seção.
    console.print(Panel(f"[bold cyan]{texto}[/bold cyan]", expand=False), justify="center")


def imprimir_sucesso(texto: str):
                    #Mensagem de sucesso em verde com ícone.
    console.print(f"\n[bold green]✔ {texto}[/bold green]\n")


def imprimir_erro(texto: str):
                    #Mensagem de erro em vermelho com ícone.
    console.print(f"[bold red]✘ {texto}[/bold red]")


def imprimir_aviso(texto: str):
                    #Mensagem de aviso em amarelo com ícone.
    console.print(f"[bold yellow]! {texto}[/bold yellow]")


def imprimir_info(texto: str):
                    #Mensagem informativa em azul.
    console.print(f"[blue]{texto}[/blue]")


def imprimir_separador():
                    #Linha divisória discreta.
    console.print("[dim]─" * 50 + "[/dim]")


def imprimir_menu(titulo: str, opcoes: dict):
    
                    #Renderiza um menu numerado dentro de um painel estilizado.
                    #opcoes: {1: 'Texto da opção', 2: '...'}
    
    texto = Text()
    for num, descricao in opcoes.items():
        texto.append(f"  [{num}] ", style="bold cyan")
        texto.append(f"{descricao}\n", style="white")
    console.print(Panel(texto, title=f"[bold magenta]{titulo}[/bold magenta]", box=box.ROUNDED))


def imprimir_continuacao(opcoes: dict):
                    #Renderiza o menu de opções de continuação com estilo menor.
    texto = Text()
    for num, descricao in opcoes.items():
        texto.append(f"  [{num}] ", style="bold cyan")
        texto.append(f"{descricao}\n", style="white")
    console.print(Panel(texto, title="[dim]Continuar[/dim]", box=box.SIMPLE))


def tabela_ativo(dados: dict, titulo: str = "Dados do Ativo"):
    
                    #Renderiza os campos de um ativo em tabela de duas colunas.
                    #dados: dicionário do ativo (ex: ativos_dicionario[id])
                    
    tabela = Table(title=titulo, box=box.ROUNDED, header_style="bold magenta", show_lines=True)
    tabela.add_column("Campo", style="bold cyan", width=18)
    tabela.add_column("Valor", style="white")

    for k, v in dados.items():
        if k == "Tipo":
            tabela.add_row(k, v.name.lower().capitalize())
        else:
            tabela.add_row(k, str(v))

    console.print(tabela)


def tabela_vulnerabilidade(dados: dict, titulo: str = "Vulnerabilidade"):
    
                    #Renderiza os campos de uma vulnerabilidade em tabela de duas colunas.
                    #dados: dicionário de uma vulnerabilidade
                    
    tabela = Table(title=titulo, box=box.ROUNDED, header_style="bold magenta", show_lines=True)
    tabela.add_column("Campo", style="bold cyan", width=18)
    tabela.add_column("Valor", style="white")

    for k, v in dados.items():
        if k in ("Severidade", "Status"):
            tabela.add_row(k, v.name.lower().capitalize())
        else:
            tabela.add_row(k, str(v))

    console.print(tabela)


def lista_ativos(ativos_dicionario: dict):
                    #Renderiza a lista de ativos cadastrados em tabela.
    tabela = Table(title="Ativos Cadastrados", box=box.ROUNDED, header_style="bold magenta")
    tabela.add_column("ID", style="bold cyan", justify="center", width=6)
    tabela.add_column("Nome", style="white")

    for k, v in ativos_dicionario.items():
        tabela.add_row(str(k), v["Nome"].lower().capitalize())

    console.print(tabela)


def lista_vulnerabilidades(lista: list):
                    #Renderiza a lista de vulnerabilidades de um ativo.
    tabela = Table(title="Vulnerabilidades do Ativo", box=box.ROUNDED, header_style="bold magenta")
    tabela.add_column("#", style="bold cyan", justify="center", width=4)
    tabela.add_column("Vulnerabilidade", style="white")
    tabela.add_column("Severidade", style="yellow", width=14)
    tabela.add_column("Status", style="blue", width=16)

    for i, vuln in enumerate(lista, start=1):
        tabela.add_row(
            str(i),
            vuln["Vulnerabilidade"],
            vuln["Severidade"].name.lower().capitalize(),
            vuln["Status"].name.lower().capitalize()
        )

    console.print(tabela)


def lista_enums(enum_class, titulo: str = "Opções"):
                    #Renderiza as opções de um Enum em tabela compacta.
    tabela = Table(title=titulo, box=box.SIMPLE, header_style="bold cyan")
    tabela.add_column("Código", justify="center", style="bold cyan", width=8)
    tabela.add_column("Descrição", style="white")

    for item in enum_class:
        tabela.add_row(str(item.value), item.name.lower().capitalize())

    console.print(tabela)


def painel_confirmacao(mensagem: str):
                    #Painel amarelo para confirmações críticas (deletar, etc.).
    console.print(Panel(
        f"[bold yellow]{mensagem}[/bold yellow]",
        title="[bold red]⚠ Confirmação[/bold red]",
        box=box.HEAVY,
        border_style="red"
    ))


# ─────────────────────────────────────────────
#  VALIDADORES 
# ─────────────────────────────────────────────

def validador_str(msg):
                    #Validador de string não vazia.
    info = console.input(f"[bold white]{msg}[/bold white]").strip()

    while not info:
        imprimir_erro("O CAMPO NÃO DEVE SER DEIXADO EM BRANCO!")
        info = console.input(f"[bold white]{msg}[/bold white]").strip()
    return info


def validador_int(msg):
                    #Validador de inteiro não vazio.
    while True:
        num_str = console.input(f"[bold white]{msg}[/bold white]").strip()

        if not num_str:
            imprimir_erro("O CAMPO NÃO DEVE SER DEIXADO EM BRANCO!")
            continue

        try:
            return int(num_str)
        except ValueError:
            imprimir_erro("DIGITE UM NÚMERO INTEIRO!")