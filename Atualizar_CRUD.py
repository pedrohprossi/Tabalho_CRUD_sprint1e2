from Modulos_adicionais import lista_vulnerabilidades
from Ativos import ativos_dicionario, TipoAtivos, vulnerabilidades_dicionario, TipoSeveridade, TipoStatus
from Modulos_salvar import salvar_ativos, salvar_vulnerabilidade
from Modulos_adicionais import (
    validador_int, validador_str, console,
    imprimir_titulo, imprimir_sucesso, imprimir_erro, imprimir_aviso,
    imprimir_menu, imprimir_continuacao,
    tabela_ativo, lista_ativos, lista_enums
)


# ─────────────────────────────────────────────
#  ATUALIZAR ATIVO
# ─────────────────────────────────────────────

def atualizar_crud(id=None):    #Atualizar ativo, id=None pq pode ser chamado do menu ou do Ler do crud
    imprimir_titulo("Atualizar Ativo")

                                # Campos disponíveis para atualização
    campo = {
        1: "Nome",
        2: "Descrição",
        3: "Responsável",
        4: "Setor",
        5: "Localização",
        6: "Tipo",
        7: "Vulnerabilidades",
        8: "Voltar ao menu",
    }
                                #Verifica se tem ativos cadastrados
    if not ativos_dicionario:
        imprimir_aviso("NENHUM ATIVO CADASTRADO NO SISTEMA!")
        return

    if id is None:              #Caso a função seja chamada do menu, pede qual ativo deseja atualizar
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

    tabela_ativo(ativos_dicionario[id], titulo=f"Ativo #{id} — Estado Atual")

    while True:                 #Pede o campo para a atualização
        imprimir_menu("Campos para Atualização", campo)

        escolha_campo = validador_int("Campo que deseja alterar: ")
        while escolha_campo not in range(1, 9):
            imprimir_erro("DIGITE UMA OPÇÃO VÁLIDA!")
            escolha_campo = validador_int("Campo que deseja alterar: ")

                    
        if escolha_campo == 1:
            ativos_dicionario[id][campo[escolha_campo]] = validador_str("Novo nome: ")

        elif escolha_campo == 2:
            ativos_dicionario[id][campo[escolha_campo]] = validador_str("Nova descrição: ")

        elif escolha_campo == 3:
            ativos_dicionario[id][campo[escolha_campo]] = validador_str("Novo responsável: ")

        elif escolha_campo == 4:
            ativos_dicionario[id][campo[escolha_campo]] = validador_str("Novo setor: ")

        elif escolha_campo == 5:
            ativos_dicionario[id][campo[escolha_campo]] = validador_str("Nova localização: ")

        elif escolha_campo == 6:
            lista_enums(TipoAtivos, titulo="Tipos de Ativo")
            while True:
                escolha_tipo = validador_int("Código do novo tipo: ")
                try:
                    tipo = TipoAtivos(escolha_tipo)
                    break
                except ValueError:
                    imprimir_erro("TIPO INVÁLIDO — ESCOLHA UM CÓDIGO DA LISTA!")
            ativos_dicionario[id][campo[escolha_campo]] = tipo

        elif escolha_campo == 7:
            atualizar_vulnerabilidade(id)

        else:
            return

        salvar_ativos()
        imprimir_sucesso("Ativo atualizado com sucesso!")

                                    #Opções de continuação
        imprimir_continuacao({
            1: "Atualizar outra informação do ativo",
            2: "Atualizar vulnerabilidades do ativo",
            3: "Voltar ao menu",
        })
        escolha_continuacao = validador_int("Opção: ")
        while escolha_continuacao not in range(1, 4):
            imprimir_erro("ESCOLHA UMA OPÇÃO EXISTENTE!")
            escolha_continuacao = validador_int("Opção: ")

        if escolha_continuacao == 1:
            continue
        elif escolha_continuacao == 2:
            atualizar_vulnerabilidade(id)
        else:
            return


# ─────────────────────────────────────────────
#  ATUALIZAR VULNERABILIDADE
# ─────────────────────────────────────────────

def atualizar_vulnerabilidade(id=None):         #Atualizar a vulnerabilidade, id=None pq pode ser chamado do menu ou do Ler vulnerabilidade do crud          
    imprimir_titulo("Atualizar Vulnerabilidade")

    if not ativos_dicionario:                   #Caso não tenha ativos
        imprimir_aviso("NENHUM ATIVO CADASTRADO NO SISTEMA!")
        return

    if id is None:                              #Caso seja chamado do menu, mostra o ativo e pede escolha
        lista_ativos(ativos_dicionario)

        while True:    
            atualizar_crud_escolha = console.input("[bold white]ID ou nome do ativo: [/bold white]").strip().lower()
            try:
                id = int(atualizar_crud_escolha)
                if id not in ativos_dicionario:
                    imprimir_erro("DIGITE UM ID VÁLIDO!")
                    continue
                break
            except ValueError:
                encontrado = False
                for k, v in ativos_dicionario.items():
                    if atualizar_crud_escolha in v["Nome"].lower():
                        id = k
                        encontrado = True
                        break
                if not encontrado:
                    imprimir_erro("DIGITE UM NOME VÁLIDO!")
                    continue
                break

    if id not in vulnerabilidades_dicionario or not vulnerabilidades_dicionario[id]:
        imprimir_aviso("ESTE ATIVO NÃO POSSUI VULNERABILIDADES REGISTRADAS!")
        return

                            #Campo de vulnerabilidades
    campo_vuln = {                  
        1: "Vulnerabilidade",
        2: "Risco",
        3: "Categoria",
        4: "Severidade",
        5: "Status",
        6: "Voltar ao menu",
    }

    while True:
                     #Lista de vulnerabilidades  e pede a escolha depois

        lista_vulnerabilidades(vulnerabilidades_dicionario[id])

        escolha_vuln = validador_int("Número da vulnerabilidade a alterar: ")
        while escolha_vuln < 1 or escolha_vuln > len(vulnerabilidades_dicionario[id]):
            imprimir_erro("ESCOLHA UMA OPÇÃO VÁLIDA!")
            escolha_vuln = validador_int("Número da vulnerabilidade a alterar: ")

        vuln_escolhida = vulnerabilidades_dicionario[id][escolha_vuln - 1]

        imprimir_menu("Campos para Atualização", campo_vuln)

                        #Escolha do campo e atualização
        escolha_campo_vuln = validador_int("Campo que deseja alterar: ")
        while escolha_campo_vuln not in range(1, 7):
            imprimir_erro("DIGITE UMA OPÇÃO VÁLIDA!")
            escolha_campo_vuln = validador_int("Campo que deseja alterar: ")

        # Lógica original preservada
        if escolha_campo_vuln == 1:
            vuln_escolhida[campo_vuln[escolha_campo_vuln]] = validador_str("Nova descrição da vulnerabilidade: ")

        elif escolha_campo_vuln == 2:
            vuln_escolhida[campo_vuln[escolha_campo_vuln]] = validador_str("Novo risco: ")

        elif escolha_campo_vuln == 3:
            vuln_escolhida[campo_vuln[escolha_campo_vuln]] = validador_str("Nova categoria: ")

        elif escolha_campo_vuln == 4:
            lista_enums(TipoSeveridade, titulo="Severidade")
            while True:
                escolha_severidade = validador_int("Código da nova severidade: ")
                try:
                    severidade = TipoSeveridade(escolha_severidade)
                    break
                except ValueError:
                    imprimir_erro("SEVERIDADE INVÁLIDA — ESCOLHA UM CÓDIGO DA LISTA!")
            vuln_escolhida[campo_vuln[escolha_campo_vuln]] = severidade

        elif escolha_campo_vuln == 5:
            lista_enums(TipoStatus, titulo="Status")
            while True:
                escolha_status = validador_int("Código do novo status: ")
                try:
                    status = TipoStatus(escolha_status)
                    break
                except ValueError:
                    imprimir_erro("STATUS INVÁLIDO — ESCOLHA UM CÓDIGO DA LISTA!")
            vuln_escolhida[campo_vuln[escolha_campo_vuln]] = status

        else:
            return

        salvar_vulnerabilidade()
        imprimir_sucesso("Vulnerabilidade atualizada com sucesso!")

                #Opções de continuação
        imprimir_continuacao({1: "Atualizar outra vulnerabilidade", 2: "Voltar ao menu"})
        escolha_continuacao = validador_int("Opção: ")
        while escolha_continuacao not in (1, 2):
            imprimir_erro("ESCOLHA UMA OPÇÃO EXISTENTE!")
            escolha_continuacao = validador_int("Opção: ")

        if escolha_continuacao == 1:
            continue
        else:
            return