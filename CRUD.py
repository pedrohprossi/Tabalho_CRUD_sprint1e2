from Ativos import ativos, TipoAtivos
from Dados import salvar_ativos
####colocar cor no codigo#####


def validador_str(msg):
    info = input(msg).strip()


    while not info:
        print('O ESPAÇO NÃO DEVE SER DEIXADO EM BRANCO!')
        info = input(msg).strip()
    return info




def validador_int(num):
    while True:
        num_str = input(num).strip()


        if not num_str:
            print('O ESPAÇO NÃO DEVE SER DEIXADO EM BRANCO!')
            continue


        try:
            return int(num_str)
        except ValueError:
            print(f'DIGITE UM NÚMERO INTEIRO!')






###########CRIAR###############
def criar_crud():
    id = validador_int('Digite o ID do novo ativo: ')
    while id in ativos:
        print('ESSE ID JÁ PERTENCE À OUTRO ATIVO!')
        id = validador_int('Digite o ID do novo ativo: ')


    nome = validador_str('Digite o nome do novo ativo: ')


    descricao = validador_str('Digite a descrição do novo ativo: ')


    responsavel = validador_str('Digite o/a responsável pelo novo ativo: ')


    setor = validador_str('Digite o setor do novo ativo: ')


    localizacao = validador_str('Digite a localização do novo ativo: ')


    for t in TipoAtivos:
        print(f'[{t.value}] = {t.name}')

    while True:
        escolha_tipo = validador_int(f'Digite o tipo do novo ativo: ')
        try:
            tipo = TipoAtivos(escolha_tipo)
            break
        except ValueError:
            print('TIPO ESCOLHIDO INVÁLIDO, ESCOLHA UM TIPO DA LISTA!')



    ativos[id] = {"nome": nome,
        "descricao": descricao,
        "responsavel": responsavel,
        "setor": setor,
        "localizacao": localizacao,
        "tipo": tipo
        }


    salvar_ativos()

    print(f'O seguinte ativo foi salvo:')
    for k, v in ativos[id].items():
        print(f'{k} = {v}')

criar_crud()