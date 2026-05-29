from Ativos import ativos_dicionario, TipoAtivos, vulnerabilidades_dicionario, TipoSeveridade, TipoStatus
from Modulos_salvar import salvar_ativos, carregar_ativos, salvar_vulnerabilidade, carregar_vulnerabilidade
from Modulos_adicionais import validador_int, validador_str




#------------------------------CRIAR CRUD-------------------------------------#



def criar_crud():                      #função de criar do CRUD

    if ativos_dicionario:
        id = max(ativos_dicionario.keys()) + 1
    else:
        id = 1


    print(f'O ID gerado foi {id}')


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



    ativos_dicionario[id] = {"Nome": nome,
        "Descrição": descricao,
        "Responsável": responsavel,
        "Setor": setor,
        "Localização": localizacao,
        "Tipo": tipo
        }



    salvar_ativos()


    print(f'O seguinte ativo foi salvo:')   #Mosstra o ativo criado
    for k, v in ativos_dicionario[id].items():
        if k == "Tipo":
            print(f'{k} = {v.name}')
        else:
            print(f'{k} = {v}')



    colocar_vulnerabilidade = validador_str('Deseja adicionar uma vulnerabilidade ao ativo? [S/N] ').upper().strip()
    while colocar_vulnerabilidade not in ('S', 'N'):
        print('ESCOLHA UMA OPÇÃO VÁLIDA!')
        colocar_vulnerabilidade = validador_str('Deseja adicionar uma vulnerabilidade ao ativo? [S/N] ').upper().strip()


    if colocar_vulnerabilidade == 'S':
        vulnerabilidades_dicionario[id] = []
        adicionar_vulnerabilidade(id)
    



#------------------------------CRIAR VULNERABILIDADE-------------------------------------#

def adicionar_vulnerabilidade(id):
    if id not in vulnerabilidades_dicionario:
        vulnerabilidades_dicionario[id] = []


    while True:

        vulnerabilidade = validador_str('Digite a vulnerabilidade do ativo: ')


        risco = validador_str('Digite o risco da vulnerabilidade, o que pode causar: ')


        categoria = validador_str('Digite a categoria da vulnerabilidade: ')


        for sev in TipoSeveridade:  # Mostra as severidades da vulnerabilidade e pede a escolha
            print(f'[{sev.value}] = {sev.name}')

        while True:
            escolha_severidade = validador_int(f'Digite a severidade da vulnerabilidade do ativo: ')
            try:
                severidade = TipoSeveridade(escolha_severidade)
                break
            except ValueError:
                print('TIPO ESCOLHIDO INVÁLIDO, ESCOLHA UM TIPO DA LISTA!')


        for sta in TipoStatus:  # Mostra os status da vulnerabilidade do ativo e pede a escolha
            print(f'[{sta.value}] = {sta.name}')

        while True:
            escolha_status = validador_int(f'Digite o o status da vulnerabilidade do ativo: ')
            try:
                status = TipoStatus(escolha_status)
                break
            except ValueError:
                print('TIPO ESCOLHIDO INVÁLIDO, ESCOLHA UM TIPO DA LISTA!')


        vulnerabilidade_temporaria = {"Vulnerabilidade" : vulnerabilidade,
            "Risco" : risco,
            "Categoria" : categoria,
            "Severidade" : severidade,
            "Status" : status
        }


        vulnerabilidades_dicionario[id].append(vulnerabilidade_temporaria)
        salvar_vulnerabilidade()


        print(f'A seguinte vulnerabilidade foi salva:')   #Mostra A vulnerabilidade criada
        for k, v in vulnerabilidade_temporaria.items():
            if k in ("Severidade", "Status"):
                print(f'{k} = {v.name}')
            else:
                print(f'{k} = {v}')


        mais_vuln = validador_str('Deseja adicionar mais uma vulnerabilidade? [S/N] ').upper().strip()
        while mais_vuln not in ('S', 'N'):
            print('ESCOLHA UMA OPÇÃO VÁLIDA!')
            mais_vuln = validador_str('Deseja adicionar mais uma vulnerabilidade? [S/N] ').upper().strip()

        if mais_vuln == 'N':
            break