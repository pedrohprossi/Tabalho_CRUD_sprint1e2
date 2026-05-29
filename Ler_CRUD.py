from Ativos import ativos_dicionario, TipoAtivos, vulnerabilidades_dicionario, TipoSeveridade, TipoStatus
from Modulos_salvar import salvar_ativos, carregar_ativos, salvar_vulnerabilidade, carregar_vulnerabilidade
from Modulos_adicionais import validador_int, validador_str
from Criar_CRUD import adicionar_vulnerabilidade
from Atualizar_CRUD import atualizar_crud





#----------------------------LER CRUD-------------------------------#


def ler_crud():

    while True:

        for k, v in ativos_dicionario.items():
            print(f'[{k}] - {v["Nome"].lower().capitalize()}')

        while True:

            ler_escolha = input('Digite o ativo deseja visualizar: ').strip().lower()

            try:
                id = int(ler_escolha)

                if id not in ativos_dicionario:
                    print('DIGITE UM ID VÁLIDO!')
                    continue

                for k, v in ativos_dicionario[id].items():
                    if k == 'Tipo':
                        print(f'{k} = {v.name.lower().capitalize()}')
                    else:
                        print(f'{k} = {v}')


            except ValueError:
                
                    encontrado = False

                    for k, v in ativos_dicionario.items():
                        if ler_escolha in v["Nome"].lower():
                            id = k
                            encontrado = True

                            for chave, valor in ativos_dicionario[k].items():
                                if chave == 'Tipo':
                                    print(f'{chave} = {valor.name.lower().capitalize()}')
                                else:
                                    print(f'{chave} = {valor}')

                    if not encontrado:
                        print(f'DIGITE UM NOME VÁLIDO!')
                        continue
                    


            print('''Opções de continuação:
[1] Atualizar ativo
[2] Ler vulnerabilidades do ativo
[3] Ler outro ativo
[4] Voltar ao menu
''')
            escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')
            while escolha_continuacao not in (1, 2, 3, 4):
                print('ESCOLHA UMA OPÇÃO EXISTENTE!')
                escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')

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






#----------------------------LER VULNERABILIDADE-------------------------------#

def ler_vulnerabilidade(id):

    if id not in vulnerabilidades_dicionario or not vulnerabilidades_dicionario[id]:
        print('O ATIVO NÃO POSSUI VULNERABILIDADES REGISTRADAS!')
        return

    while True: 

        print('Vulnerabilidade: ')
        for i, vuln in enumerate(vulnerabilidades_dicionario[id], start=1):
            print(f'[{i}] {vuln["Vulnerabilidade"]}')

        escolha_vulnerabilidade = validador_int('Escolha a vulnerabilidade que deseja ver: ')
        while escolha_vulnerabilidade < 1 or escolha_vulnerabilidade > len(vulnerabilidades_dicionario[id]):
            print('DIGITE UMA OPÇÃO VÁLIDA!')
            escolha_vulnerabilidade = validador_int('Escolha a vulnerabilidade que deseja ver: ')

        vuln_escolhida = vulnerabilidades_dicionario[id][escolha_vulnerabilidade - 1]

        for k, v in vuln_escolhida.items():
            if k == 'Severidade' or k == 'Status':
                print(f'{k} = {v.name.lower().capitalize()}')
            else:
                print(f'{k} = {v}')

        print('''Opções de continuação:
              
[1] Atualizar vulnerabilidade
[2] Ler outra vulnerabilidade do ativo
[3] Voltar ao menu
''')
        escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')
        while escolha_continuacao not in (1, 2, 3):
            print('ESCOLHA UMA OPÇÃO EXISTENTE!')
            escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')

        if escolha_continuacao == 1:
            atualizar_vulnerabilidade(id)
            return


        elif escolha_continuacao == 2:
            continue

        else:
            return

        