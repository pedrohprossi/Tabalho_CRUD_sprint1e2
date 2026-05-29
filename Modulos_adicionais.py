from Ativos import ativos_dicionario, TipoAtivos, vulnerabilidades_dicionario, TipoSeveridade, TipoStatus
from Modulos_salvar import salvar_ativos, carregar_ativos, salvar_vulnerabilidade, carregar_vulnerabilidade
####colocar cor no codigo#####


def validador_str(msg):      #Validador de string
    info = input(msg).strip()


    while not info:
        print('O ESPAÇO NÃO DEVE SER DEIXADO EM BRANCO!')
        info = input(msg).strip()
    return info




def validador_int(num):       #validador string + validador intenger
    while True:
        num_str = input(num).strip()


        if not num_str:
            print('O ESPAÇO NÃO DEVE SER DEIXADO EM BRANCO!')
            continue


        try:
            return int(num_str)
        except ValueError:
            print(f'DIGITE UM NÚMERO INTEIRO!')










