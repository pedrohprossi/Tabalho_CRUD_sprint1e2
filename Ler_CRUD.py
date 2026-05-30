from Ativos import ativos_dicionario, TipoAtivos, vulnerabilidades_dicionario, TipoSeveridade, TipoStatus
from Modulos_salvar import salvar_ativos, carregar_ativos, salvar_vulnerabilidade, carregar_vulnerabilidade
from Modulos_adicionais import validador_int, validador_str
from Criar_CRUD import adicionar_vulnerabilidade
from Atualizar_CRUD import atualizar_crud, atualizar_vulnerabilidade





#----------------------------LER CRUD-------------------------------#


def ler_crud():    #Le os ativos

    while True:

        for k, v in ativos_dicionario.items():              #Mostra os ativos para escolha
            print(f'[{k}] - {v["Nome"].lower().capitalize()}')

        while True:
            #Escolha do ativo com tratamento try e except para aceitar id ou nome
            ler_escolha = input('Digite o ativo deseja visualizar: ').strip().lower()

            try:
                id = int(ler_escolha)

                if id not in ativos_dicionario:
                    print('DIGITE UM ID VÁLIDO!')
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
                        print(f'DIGITE UM NOME VÁLIDO!')
                        continue

        
        for k, v in ativos_dicionario[id].items():          #Mostra o ativo
            if k == 'Tipo':
                print(f'{k} = {v.name.lower().capitalize()}')
            else:
                print(f'{k} = {v}')



            #Opções de continuação, coloquei para atualizar por aqui também
            print('''Opções de continuação:
[1] Atualizar ativo
[2] Ler vulnerabilidades do ativo
[3] Ler outro ativo
[4] Voltar ao menu
''')
            escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')
            
            while escolha_continuacao not in range(1, 5):

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

def ler_vulnerabilidade(id):       #Le as vulnerabilidades

    if id not in vulnerabilidades_dicionario or not vulnerabilidades_dicionario[id]:    #Caso o ativo não tenha vulnerabilidade
        print('O ATIVO NÃO POSSUI VULNERABILIDADES REGISTRADAS!')
        return

    while True: 

        print('Vulnerabilidade: ')
        for i, vuln in enumerate(vulnerabilidades_dicionario[id], start=1): #Mostra as vulnerabilidades para escolha de leitura, como é uma lista, colocoquei o enumarate para enumerar ela e começar do 1
            print(f'[{i}] - {vuln["Vulnerabilidade"]}')

        #Escolha da vulnerabilidade, funciona colocando a opção ou a vulnerabilidade
        escolha_vulnerabilidade = input('Escolha a vulnerabilidade que deseja ver: ').lower().strip()

        try: 
            vn = int(escolha_vulnerabilidade)
            if vn < 1 or vn > len(vulnerabilidades_dicionario[id]):
                    print('DIGITE UM ID VÁLIDO!')
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
                    print(f'DIGITE UM VULNERABILIDADE VÁLIDA!')
                    continue    


        vuln_escolhida = vulnerabilidades_dicionario[id][vn - 1]  #Diminui um para compatilidade com a lista

        for k, v in vuln_escolhida.items():  #Mostra a vulnerabilidade
            if k == 'Severidade' or k == 'Status':
                print(f'{k} = {v.name.lower().capitalize()}')
            else:
                print(f'{k} = {v}')


        #Opções de continuação, coloquei para atualizar as vulnerabilidades por aqui também
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