from Ativos import ativos_dicionario, TipoAtivos, vulnerabilidades_dicionario, TipoSeveridade, TipoStatus
from Modulos_salvar import salvar_ativos, carregar_ativos, salvar_vulnerabilidade, carregar_vulnerabilidade
from Modulos_adicionais import validador_int, validador_str






#----------------------------LER CRUD-------------------------------#


def ler_crud():

    while True:

        for i in ativos_dicionario:
            print(f'[{i}] - {i["Nome"].lower().capitalize()}')

        while True:

            ler_escolha = input('Digite o ativo deseja visualizar: ').strip().lower()

            try:
                id = int(ler_escolha)

                while id not in ativos_dicionario:
                    print('DIGITE UM ID VÁLIDO!')

                for k, v in ativos_dicionario[id]:
                    if k == 'Tipo':
                        print(f'{k} = {v.name.lower().capitalize()}')
                    else:
                        print(f'{k} = {v}')


            except ValueError:
                while True:
                    n = 0
                    for d in ativos_dicionario:
                        if ler_escolha != d["Nome"].lower():
                            n += 1
                    break

                if len(ativos_dicionario) == n:
                    print(f'DIGITE UM NOME EXISTENTE!')
                    continue


                for i in ativos_dicionario:
                    if i["Nome"].lower() == ler_escolha:

                        for k, v in ativos_dicionario[i]:
                            if k == 'Tipo':
                                print(f'{k} = {v.name.lower().capitalize()}')
                            else:
                                print(f'{k} = {v}')


            print('''Opções de continuação:
[1] Atualizar ativo
[2] Ler vulnerabilidades do ativo
[3] Ler outro ativo
[4] Voltar ao menu
''')
            escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')
            while escolha_continuacao not in (1, 2, 3, 4):
                print('ESCOLHA UMA OPÇÃO EXISTENTE')
                escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')

            if escolha_continuacao == 1:
                atualizar_crud(id)
                voltar_menu()


            elif escolha_continuacao == 2:
                ler_vulnerabilidade(id)
                voltar_menu()

            elif escolha_continuacao == 3:
                break

            else:
                voltar_menu()






#----------------------------LER VULNERABILIDADE-------------------------------#