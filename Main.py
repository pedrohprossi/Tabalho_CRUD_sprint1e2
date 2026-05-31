from Ativos import ativos_dicionario, vulnerabilidades_dicionario
from Modulos_salvar import carregar_ativos, carregar_vulnerabilidade, inicializar_banco
from Modulos_adicionais import (
    validador_int, console,
    imprimir_titulo, imprimir_menu, imprimir_separador, imprimir_sucesso
)
from Criar_CRUD import criar_crud, adicionar_vulnerabilidade
from Ler_CRUD import ler_crud, ler_vulnerabilidade
from Atualizar_CRUD import atualizar_crud, atualizar_vulnerabilidade
from Deletar_CRUD import deletar_crud, deletar_vulnerabilidade

from rich.panel import Panel
from rich.text import Text
from rich import box


# ─────────────────────────────────────────────
#  TELA DE BOAS-VINDAS
# ─────────────────────────────────────────────

boas_vindas = Text(justify="center")
boas_vindas.append("\n  Sistema de Inventário de Segurança\n", style="bold cyan")
boas_vindas.append("  Gestão de Ativos e Vulnerabilidades de TI\n", style="dim white")
boas_vindas.append("  Cibersegurança — UFU  2026/1\n", style="dim")

console.print(Panel(boas_vindas, box=box.DOUBLE_EDGE, border_style="cyan"))


# ─────────────────────────────────────────────
#  INICIALIZAÇÃO DO BANCO
# ─────────────────────────────────────────────

inicializar_banco()
ativos_dicionario.update(carregar_ativos())
vulnerabilidades_dicionario.update(carregar_vulnerabilidade())


# ─────────────────────────────────────────────
#  MENUS — dicionários para imprimir_menu()
# ─────────────────────────────────────────────

MENU_PRINCIPAL = {
    1: "Cadastrar",
    2: "Ler / Consultar",
    3: "Atualizar",
    4: "Deletar",
    5: "Sair do programa",
}

MENU_CADASTRAR = {1: "Cadastrar um ativo", 2: "Cadastrar uma vulnerabilidade"}
MENU_LER      = {1: "Ler um ativo",        2: "Ler uma vulnerabilidade"}
MENU_ATUALIZAR = {1: "Atualizar um ativo",  2: "Atualizar uma vulnerabilidade"}
MENU_DELETAR  = {1: "Deletar um ativo",     2: "Deletar uma vulnerabilidade"}


# ─────────────────────────────────────────────
#  LOOP PRINCIPAL  (lógica original preservada)
# ─────────────────────────────────────────────

while True:
    imprimir_separador()
    imprimir_menu("Menu Principal", MENU_PRINCIPAL)

    escolha_menu = validador_int("Digite a ação que deseja executar: ")
    while escolha_menu not in range(1, 6):
        from Modulos_adicionais import imprimir_erro
        imprimir_erro("ESCOLHA UMA OPÇÃO VÁLIDA!")
        escolha_menu = validador_int("Digite a ação que deseja executar: ")


    if escolha_menu == 1:
        imprimir_menu("Cadastrar", MENU_CADASTRAR)
        escolha_cadastrar = validador_int("Digite o que deseja cadastrar: ")
        while escolha_cadastrar not in (1, 2):
            from Modulos_adicionais import imprimir_erro
            imprimir_erro("ESCOLHA UMA OPÇÃO VÁLIDA!")
            escolha_cadastrar = validador_int("Digite o que deseja cadastrar: ")

        if escolha_cadastrar == 1:
            criar_crud()
        else:
            adicionar_vulnerabilidade(id=None)


    elif escolha_menu == 2:
        imprimir_menu("Ler / Consultar", MENU_LER)
        escolha_ler = validador_int("Digite o que deseja ler: ")
        while escolha_ler not in (1, 2):
            from Modulos_adicionais import imprimir_erro
            imprimir_erro("ESCOLHA UMA OPÇÃO VÁLIDA!")
            escolha_ler = validador_int("Digite o que deseja ler: ")

        if escolha_ler == 1:
            ler_crud()
        else:
            ler_vulnerabilidade(id=None)


    elif escolha_menu == 3:
        imprimir_menu("Atualizar", MENU_ATUALIZAR)
        escolha_atualizar = validador_int("Digite o que deseja atualizar: ")
        while escolha_atualizar not in (1, 2):
            from Modulos_adicionais import imprimir_erro
            imprimir_erro("ESCOLHA UMA OPÇÃO VÁLIDA!")
            escolha_atualizar = validador_int("Digite o que deseja atualizar: ")

        if escolha_atualizar == 1:
            atualizar_crud()
        else:
            atualizar_vulnerabilidade(id=None)


    elif escolha_menu == 4:
        imprimir_menu("Deletar", MENU_DELETAR)
        escolha_deletar = validador_int("Digite o que deseja deletar: ")
        while escolha_deletar not in (1, 2):
            from Modulos_adicionais import imprimir_erro
            imprimir_erro("ESCOLHA UMA OPÇÃO VÁLIDA!")
            escolha_deletar = validador_int("Digite o que deseja deletar: ")

        if escolha_deletar == 1:
            deletar_crud()
        else:
            deletar_vulnerabilidade()


    elif escolha_menu == 5:
        imprimir_sucesso("Encerrando o programa. Até logo!")
        break