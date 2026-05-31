from Ativos import ativos_dicionario, vulnerabilidades_dicionario
from Modulos_adicionais import (
    validador_int, console,
    imprimir_titulo, imprimir_erro, imprimir_aviso,
    imprimir_continuacao,
    tabela_ativo, tabela_vulnerabilidade,
    lista_ativos, lista_vulnerabilidades
)
from Atualizar_CRUD import atualizar_crud, atualizar_vulnerabilidade


# ─────────────────────────────────────────────
#  LER ATIVO
# ─────────────────────────────────────────────

def ler_crud():
    while True:
        imprimir_titulo("Consultar Ativo")

                                #Caso não tenha ativo
        if not ativos_dicionario:
            imprimir_aviso("NENHUM ATIVO CADASTRADO NO SISTEMA!")
            return

        lista_ativos(ativos_dicionario)
                                #Mostra ativo e pede escolha
        while True:
            ler_escolha = console.input("[bold white]ID ou nome do ativo: [/bold white]").strip().lower()
            try:
                id = int(ler_escolha)
                if id not in ativos_dicionario:
                    imprimir_erro("DIGITE UM ID VÁLIDO!")
                    continue
                break
            except ValueError:
                encontrado = False
                for k, v in ativos_dicionario.items():
                    if ler_escolha in v["Nome"].lower():
                        id = k
                        encontrado = True
                        break
                if not encontrado:
                    imprimir_erro("DIGITE UM NOME VÁLIDO!")
                    continue
                break

                                #Exibição do ativo
        tabela_ativo(ativos_dicionario[id], titulo=f"Ativo #{id}")
                                
                                #Opções continuação
        imprimir_continuacao({
            1: "Atualizar ativo",
            2: "Ler vulnerabilidades do ativo",
            3: "Ler outro ativo",
            4: "Voltar ao menu",
        })
        escolha_continuacao = validador_int("Opção: ")
        while escolha_continuacao not in range(1, 5):
            imprimir_erro("ESCOLHA UMA OPÇÃO EXISTENTE!")
            escolha_continuacao = validador_int("Opção: ")

        if escolha_continuacao == 1:
            atualizar_crud(id)
            return
        elif escolha_continuacao == 2:
            ler_vulnerabilidade(id)
            return
        elif escolha_continuacao == 3:
            break
        else:
            return


# ─────────────────────────────────────────────
#  LER VULNERABILIDADE
# ─────────────────────────────────────────────

def ler_vulnerabilidade(id=None):           #Ler vulnerabilidade, id=None pq pode ser chamado do menu ou do Ler do crud
    imprimir_titulo("Consultar Vulnerabilidade")

    if id is None:                          #Mostra os ativos e pede escolha
        if not ativos_dicionario:           #Caso nã tenha nenhum ativo
            imprimir_aviso("NENHUM ATIVO CADASTRADO NO SISTEMA!")
            return

        lista_ativos(ativos_dicionario)

        while True:
            ler_escolha = console.input("[bold white]ID ou nome do ativo: [/bold white]").strip().lower()
            try:
                id = int(ler_escolha)
                if id not in ativos_dicionario:
                    imprimir_erro("DIGITE UM ID VÁLIDO!")
                    continue
                break
            except ValueError:
                encontrado = False
                for k, v in ativos_dicionario.items():
                    if ler_escolha in v["Nome"].lower():
                        id = k
                        encontrado = True
                        break
                if not encontrado:
                    imprimir_erro("DIGITE UM NOME VÁLIDO!")
                    continue
                break

                                        #Caso não tenha vulnerabilidade registrada
    if id not in vulnerabilidades_dicionario or not vulnerabilidades_dicionario[id]:
        imprimir_aviso("O ATIVO NÃO POSSUI VULNERABILIDADES REGISTRADAS!")
        return

    while True:                         #Mostra as vulnerabilidades e pede escolha
        lista_vulnerabilidades(vulnerabilidades_dicionario[id])

        while True:
            escolha_vulnerabilidade = console.input("[bold white]Número ou nome da vulnerabilidade: [/bold white]").lower().strip()
            try:
                vn = int(escolha_vulnerabilidade)
                if vn < 1 or vn > len(vulnerabilidades_dicionario[id]):
                    imprimir_erro("DIGITE UM NÚMERO VÁLIDO!")
                    continue
                break
            except ValueError:
                encontrado = False
                for k, v in enumerate(vulnerabilidades_dicionario[id], start=1):
                    if escolha_vulnerabilidade in v["Vulnerabilidade"].lower():
                        vn = k
                        encontrado = True
                        break
                if not encontrado:
                    imprimir_erro("DIGITE UMA VULNERABILIDADE VÁLIDA!")
                    continue
                break

        vuln_escolhida = vulnerabilidades_dicionario[id][vn - 1]

                                            #Exibição da vulnerabilidade
        tabela_vulnerabilidade(vuln_escolhida, titulo=f"Vulnerabilidade #{vn}")


                                            #Opção de continuação
        imprimir_continuacao({
            1: "Atualizar vulnerabilidade",
            2: "Ler outra vulnerabilidade do ativo",
            3: "Voltar ao menu",
        })
        escolha_continuacao = validador_int("Opção: ")
        while escolha_continuacao not in (1, 2, 3):
            imprimir_erro("ESCOLHA UMA OPÇÃO EXISTENTE!")
            escolha_continuacao = validador_int("Opção: ")

        if escolha_continuacao == 1:
            atualizar_vulnerabilidade(id)
            return
        elif escolha_continuacao == 2:
            continue
        else:
            return