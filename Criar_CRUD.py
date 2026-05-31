from Ativos import ativos_dicionario, TipoAtivos, vulnerabilidades_dicionario, TipoSeveridade, TipoStatus
from Modulos_salvar import salvar_ativos, salvar_vulnerabilidade
from Modulos_adicionais import (
    validador_int, validador_str, console,
    imprimir_titulo, imprimir_sucesso, imprimir_erro, imprimir_aviso,
    imprimir_menu, imprimir_continuacao,
    tabela_ativo, tabela_vulnerabilidade, lista_ativos, lista_enums
)
import sqlite3


# ─────────────────────────────────────────────
#  GERAÇÃO SEGURA DE ID  (lógica original)
# ─────────────────────────────────────────────

def obter_id() -> int:
    from Modulos_salvar import DB_NAME, conectar

    id_memoria = max(ativos_dicionario.keys()) + 1 if ativos_dicionario else 1

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(id) FROM ativos")
        resultado = cursor.fetchone()
        conn.close()
        id_banco = (resultado[0] or 0) + 1
    except sqlite3.OperationalError:
        id_banco = 1

    return max(id_memoria, id_banco)


# ─────────────────────────────────────────────
#  CRIAR ATIVO
# ─────────────────────────────────────────────

def criar_crud():
    imprimir_titulo("Cadastrar Novo Ativo")

    id = obter_id()
    console.print(f"[bold blue]  ID gerado automaticamente: [bold cyan]{id}[/bold cyan][/bold blue]\n")

    # Coleta de dados — lógica original preservada
    nome        = validador_str("Nome do ativo: ")
    descricao   = validador_str("Descrição: ")
    responsavel = validador_str("Responsável: ")
    setor       = validador_str("Setor: ")
    localizacao = validador_str("Localização: ")

    # Seleção de tipo com tabela visual
    lista_enums(TipoAtivos, titulo="Tipos de Ativo")
    while True:
        escolha_tipo = validador_int("Digite o código do tipo: ")
        try:
            tipo = TipoAtivos(escolha_tipo)
            break
        except ValueError:
            imprimir_erro("TIPO INVÁLIDO — ESCOLHA UM CÓDIGO DA LISTA!")

    # Salva no dicionário — lógica original
    ativos_dicionario[id] = {
        "Nome": nome,
        "Descrição": descricao,
        "Responsável": responsavel,
        "Setor": setor,
        "Localização": localizacao,
        "Tipo": tipo,
    }
    salvar_ativos()

    # Confirmação visual em tabela
    imprimir_sucesso("Ativo cadastrado com sucesso!")
    tabela_ativo(ativos_dicionario[id], titulo=f"Ativo #{id} — Salvo")

    # Opções de continuação — estrutura original
    imprimir_continuacao({1: "Cadastrar vulnerabilidade", 2: "Voltar ao menu"})
    escolha_continuacao = validador_int("Opção: ")
    while escolha_continuacao not in (1, 2):
        imprimir_erro("ESCOLHA UMA OPÇÃO EXISTENTE!")
        escolha_continuacao = validador_int("Opção: ")

    if escolha_continuacao == 1:
        vulnerabilidades_dicionario[id] = []
        adicionar_vulnerabilidade(id)
    else:
        vulnerabilidades_dicionario[id] = []
        return


# ─────────────────────────────────────────────
#  CRIAR VULNERABILIDADE
# ─────────────────────────────────────────────

def adicionar_vulnerabilidade(id=None):
    imprimir_titulo("Cadastrar Vulnerabilidade")

    if id is None:
        lista_ativos(ativos_dicionario)

        while True:
            criar_escolha = console.input("[bold white]ID ou nome do ativo: [/bold white]").strip().lower()
            try:
                id = int(criar_escolha)
                if id not in ativos_dicionario:
                    imprimir_erro("DIGITE UM ID VÁLIDO!")
                    continue
                break
            except ValueError:
                encontrado = False
                for k, v in ativos_dicionario.items():
                    if criar_escolha in v["Nome"].lower():
                        id = k
                        encontrado = True
                        break
                if not encontrado:
                    imprimir_erro("DIGITE UM NOME VÁLIDO!")
                    continue
                break

    if id not in vulnerabilidades_dicionario:
        vulnerabilidades_dicionario[id] = []

    while True:
        # Coleta de dados — lógica original
        vulnerabilidade = validador_str("Vulnerabilidade: ")
        risco           = validador_str("Risco (o que pode causar): ")
        categoria       = validador_str("Categoria: ")

        lista_enums(TipoSeveridade, titulo="Severidade")
        while True:
            escolha_severidade = validador_int("Código da severidade: ")
            try:
                severidade = TipoSeveridade(escolha_severidade)
                break
            except ValueError:
                imprimir_erro("SEVERIDADE INVÁLIDA — ESCOLHA UM CÓDIGO DA LISTA!")

        lista_enums(TipoStatus, titulo="Status")
        while True:
            escolha_status = validador_int("Código do status: ")
            try:
                status = TipoStatus(escolha_status)
                break
            except ValueError:
                imprimir_erro("STATUS INVÁLIDO — ESCOLHA UM CÓDIGO DA LISTA!")

        vulnerabilidade_temporaria = {
            "Vulnerabilidade": vulnerabilidade,
            "Risco": risco,
            "Categoria": categoria,
            "Severidade": severidade,
            "Status": status,
        }

        vulnerabilidades_dicionario[id].append(vulnerabilidade_temporaria)
        salvar_vulnerabilidade()

        imprimir_sucesso("Vulnerabilidade cadastrada com sucesso!")
        tabela_vulnerabilidade(vulnerabilidade_temporaria, titulo="Vulnerabilidade Salva")

        imprimir_continuacao({1: "Cadastrar outra vulnerabilidade", 2: "Voltar ao menu"})
        escolha_continuacao = validador_int("Opção: ")
        while escolha_continuacao not in (1, 2):
            imprimir_erro("ESCOLHA UMA OPÇÃO EXISTENTE!")
            escolha_continuacao = validador_int("Opção: ")

        if escolha_continuacao == 1:
            continue
        else:
            return