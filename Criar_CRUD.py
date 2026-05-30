from Ativos import ativos_dicionario, TipoAtivos, vulnerabilidades_dicionario, TipoSeveridade, TipoStatus
from Modulos_salvar import salvar_ativos, carregar_ativos, salvar_vulnerabilidade, carregar_vulnerabilidade
from Modulos_adicionais import validador_int, validador_str




#------------------------------CRIAR CRUD-------------------------------------#



def criar_crud():                      #função de criar do CRUD

    if ativos_dicionario:           #Gera o id do ativo, se não existir nenhum ativo o id = 1
        id = max(ativos_dicionario.keys()) + 1
    else:
        id = 1


    print(f'O ID gerado foi {id}')  #Mostra o id gerado


    #Criação das informações do ativo
    nome = validador_str('Digite o nome do novo ativo: ')

    descricao = validador_str('Digite a descrição do novo ativo: ')

    responsavel = validador_str('Digite o/a responsável pelo novo ativo: ')

    setor = validador_str('Digite o setor do novo ativo: ')

    localizacao = validador_str('Digite a localização do novo ativo: ')



    for t in TipoAtivos:              #Mostra os tipos de ativos e pede a escolha
        print(f'[{t.value}] = {t.name}')

    while True:
        escolha_tipo = validador_int(f'Digite o tipo do novo ativo: ')
        try:
            tipo = TipoAtivos(escolha_tipo)
            break
        except ValueError:
            print('TIPO ESCOLHIDO INVÁLIDO, ESCOLHA UM TIPO DA LISTA!')



    ativos_dicionario[id] = {"Nome": nome,    #Coloca as informações criadas no dicionario
        "Descrição": descricao,
        "Responsável": responsavel,
        "Setor": setor,
        "Localização": localizacao,
        "Tipo": tipo
        }



    salvar_ativos()


    print(f'O seguinte ativo foi salvo:')   #Mostra o ativo criado
    for k, v in ativos_dicionario[id].items():
        if k == "Tipo":
            print(f'{k} = {v.name}')
        else:
            print(f'{k} = {v}')




    # Opções de continuação
    print('''Opções de continuação:

[1] Cadastrar vulnerabilidade
[2] Voltar ao menu
''')

    escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')

    while escolha_continuacao not in (1, 2):
        print('ESCOLHA UMA OPÇÃO EXISTENTE!')
        escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')

    if escolha_continuacao == 1:
        vulnerabilidades_dicionario[id] = []
        adicionar_vulnerabilidade(id)

    else:
        return







#------------------------------CRIAR VULNERABILIDADE-------------------------------------#

def adicionar_vulnerabilidade(id=None):              #Cria vulnerabilidade
    if id not in vulnerabilidades_dicionario:   #Caso crie a vulnerabilidade direto do menu e o ativo não tenha nenhuma outra
        vulnerabilidades_dicionario[id] = []


    if id == None:
            for k, v in ativos_dicionario.items():
                print(f'{k} = {v["Nome"]}')

            while True:
                # Escolha do ativo com tratamento try e except para aceitar id ou nome
                deletar_escolha = input('Digite o ativo que deseja deletar a vulnerabilidade: ').strip().lower()

                try:
                    id = int(deletar_escolha)

                    if id not in ativos_dicionario:
                        print('DIGITE UM ID VÁLIDO!')
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
                        print(f'DIGITE UM NOME VÁLIDO!')
                        continue


    while True:

        #Informações das vulnerabilidades
        vulnerabilidade = validador_str('Digite a vulnerabilidade do ativo: ')


        risco = validador_str('Digite o risco da vulnerabilidade, o que pode causar: ')


        categoria = validador_str('Digite a categoria da vulnerabilidade: ')


        for sev in TipoSeveridade:      # Mostra as severidades da vulnerabilidade e pede a escolha
            print(f'[{sev.value}] = {sev.name}')

        while True:
            escolha_severidade = validador_int(f'Digite a severidade da vulnerabilidade do ativo: ')
            try:
                severidade = TipoSeveridade(escolha_severidade)
                break
            except ValueError:
                print('TIPO ESCOLHIDO INVÁLIDO, ESCOLHA UM TIPO DA LISTA!')


        for sta in TipoStatus:       # Mostra os status da vulnerabilidade do ativo e pede a escolha
            print(f'[{sta.value}] = {sta.name}')

        while True:
            escolha_status = validador_int(f'Digite o o status da vulnerabilidade do ativo: ')
            try:
                status = TipoStatus(escolha_status)
                break
            except ValueError:
                print('TIPO ESCOLHIDO INVÁLIDO, ESCOLHA UM TIPO DA LISTA!')


        vulnerabilidade_temporaria = {"Vulnerabilidade" : vulnerabilidade,              #Salva em dicionario a vulnerabilidade
            "Risco" : risco,
            "Categoria" : categoria,
            "Severidade" : severidade,
            "Status" : status
        }


        vulnerabilidades_dicionario[id].append(vulnerabilidade_temporaria)        #Salva na lista principal
        salvar_vulnerabilidade()


        print(f'A seguinte vulnerabilidade foi salva:')   #Mostra A vulnerabilidade criada
        for k, v in vulnerabilidade_temporaria.items():
            if k in ("Severidade", "Status"):
                print(f'{k} = {v.name}')
            else:
                print(f'{k} = {v}')



            # Opções de continuação
            print('''Opções de continuação:

        [1] Cadastrar outra vulnerabilidade
        [2] Voltar ao menu
        ''')

            escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')

            while escolha_continuacao not in (1, 2):
                print('ESCOLHA UMA OPÇÃO EXISTENTE!')
                escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')

            if escolha_continuacao == 1:
                continue

            else:
                return