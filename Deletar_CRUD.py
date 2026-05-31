from Ativos import ativos_dicionario, vulnerabilidades_dicionario
from Modulos_salvar import salvar_ativos, salvar_vulnerabilidade
from Modulos_adicionais import (
    validador_int, validador_str, console,
    imprimir_titulo, imprimir_sucesso, imprimir_erro, imprimir_aviso,
    imprimir_menu, imprimir_continuacao,
    tabela_ativo, tabela_vulnerabilidade,
    lista_ativos, lista_vulnerabilidades, painel_confirmacao
)


# ─────────────────────────────────────────────
#  DELETAR ATIVO
# ─────────────────────────────────────────────

def deletar_crud():
    while True:
        imprimir_titulo("Deletar Ativo")

        if not ativos_dicionario:
            imprimir_aviso("NENHUM ATIVO CADASTRADO NO SISTEMA!")
            return

        lista_ativos(ativos_dicionario)

        while True:
            deletar_escolha = console.input("[bold white]ID ou nome do ativo: [/bold white]").strip().lower()
            try:
                id = int(deletar_escolha)
                if id not in ativos_dicionario:
                    imprimir_erro("DIGITE UM ID VÁLIDO!")
                    continue
                break
            except ValueError:
                encontrado = False
                for k, v in ativos_dicionario.items():
                    if deletar_escolha in v["Nome"].lower():
                        id = k
                        encontrado = True
                        break
                if not encontrado:
                    imprimir_erro("DIGITE UM NOME VÁLIDO!")
                    continue
                break

        tabela_ativo(ativos_dicionario[id], titulo=f"Ativo #{id} — A ser deletado")

        # Painel de alerta antes da confirmação
        painel_confirmacao(f'Tem certeza que deseja deletar o ativo "{ativos_dicionario[id]["Nome"]}"?\nEsta ação removerá também todas as vulnerabilidades associadas.')

        confirmacao_deletar = validador_str("Confirme [S/N]: ").upper()
        while confirmacao_deletar not in ("S", "N"):
            imprimir_erro("DIGITE UMA OPÇÃO VÁLIDA!")
            confirmacao_deletar = validador_str("Confirme [S/N]: ").upper()

        # Lógica original de deleção preservada
        if confirmacao_deletar == "S":
            del ativos_dicionario[id]
            if id in vulnerabilidades_dicionario:
                del vulnerabilidades_dicionario[id]
            salvar_ativos()
            salvar_vulnerabilidade()
            imprimir_sucesso("ATIVO DELETADO COM SUCESSO!")
            return
        else:
            return


# ─────────────────────────────────────────────
#  DELETAR VULNERABILIDADE
# ─────────────────────────────────────────────

def deletar_vulnerabilidade(id=None):
    while True:
        imprimir_titulo("Deletar Vulnerabilidade")

        if not ativos_dicionario:
            imprimir_aviso("NENHUM ATIVO CADASTRADO NO SISTEMA!")
            return

        if id is None:
            lista_ativos(ativos_dicionario)

            while True:
                deletar_escolha = console.input("[bold white]ID ou nome do ativo: [/bold white]").strip().lower()
                try:
                    id = int(deletar_escolha)
                    if id not in ativos_dicionario:
                        imprimir_erro("DIGITE UM ID VÁLIDO!")
                        continue
                    break
                except ValueError:
                    encontrado = False
                    for k, v in ativos_dicionario.items():
                        if deletar_escolha in v["Nome"].lower():
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

        imprimir_menu("Opções de Remoção", {
            1: "Apagar TODAS as vulnerabilidades do ativo",
            2: "Apagar apenas uma vulnerabilidade",
        })
        escolha_remocao = validador_int("Opção: ")
        while escolha_remocao not in (1, 2):
            imprimir_erro("DIGITE UMA OPÇÃO VÁLIDA!")
            escolha_remocao = validador_int("Opção: ")

        if escolha_remocao == 1:
            lista_vulnerabilidades(vulnerabilidades_dicionario[id])

            painel_confirmacao("Tem certeza que deseja deletar TODAS as vulnerabilidades acima?")
            confirmacao_deletar_tudo = validador_str("Confirme [S/N]: ").upper()
            while confirmacao_deletar_tudo not in ("S", "N"):
                imprimir_erro("DIGITE UMA OPÇÃO VÁLIDA!")
                confirmacao_deletar_tudo = validador_str("Confirme [S/N]: ").upper()

            if confirmacao_deletar_tudo == "S":
                del vulnerabilidades_dicionario[id]
                salvar_vulnerabilidade()
                imprimir_sucesso("TODAS AS VULNERABILIDADES DELETADAS COM SUCESSO!")
                return
            else:
                return

        else:
            lista_vulnerabilidades(vulnerabilidades_dicionario[id])

            while True:
                deletar_escolha_vulnerabilidade = console.input(
                    "[bold white]Número ou nome da vulnerabilidade: [/bold white]"
                ).lower().strip()

                try:
                    vn = int(deletar_escolha_vulnerabilidade)
                    if vn < 1 or vn > len(vulnerabilidades_dicionario[id]):
                        imprimir_erro("DIGITE UM NÚMERO VÁLIDO!")
                        continue
                    break
                except ValueError:
                    encontrado = False
                    for k, v in enumerate(vulnerabilidades_dicionario[id], start=1):
                        if deletar_escolha_vulnerabilidade in v["Vulnerabilidade"].lower():
                            vn = k
                            encontrado = True
                            break
                    if not encontrado:
                        imprimir_erro("DIGITE UMA VULNERABILIDADE VÁLIDA!")
                        continue
                    break

            vuln_escolhida = vulnerabilidades_dicionario[id][vn - 1]

            tabela_vulnerabilidade(vuln_escolhida, titulo="Vulnerabilidade a ser deletada")
            painel_confirmacao(f'Tem certeza que deseja deletar "{vuln_escolhida["Vulnerabilidade"]}"?')

            confirmacao_deletar = validador_str("Confirme [S/N]: ").upper()
            while confirmacao_deletar not in ("S", "N"):
                imprimir_erro("DIGITE UMA OPÇÃO VÁLIDA!")
                confirmacao_deletar = validador_str("Confirme [S/N]: ").upper()

            if confirmacao_deletar == "S":
                vulnerabilidades_dicionario[id].pop(vn - 1)
                salvar_vulnerabilidade()
                imprimir_sucesso("VULNERABILIDADE DELETADA COM SUCESSO!")
                return
            else:
                return