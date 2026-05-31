#------------------VALIDADOR DE STRING-----------------#

def validador_str(msg):      
    info = input(msg).strip()


    while not info:
        print('O ESPAÇO NÃO DEVE SER DEIXADO EM BRANCO!')
        info = input(msg).strip()
    return info




#--------------VALIDADOR DE STRING E INTEIRO--------------#

def validador_int(num):       #validador string + validador de inteiro
    while True:
        num_str = input(num).strip()


        if not num_str:
            print('O ESPAÇO NÃO DEVE SER DEIXADO EM BRANCO!')
            continue


        try:
            return int(num_str)
        except ValueError:
            print(f'DIGITE UM NÚMERO INTEIRO!')



