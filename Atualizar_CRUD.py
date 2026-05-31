from Ativos import ativos_dicionario, TipoAtivos, vulnerabilidades_dicionario, TipoSeveridade, TipoStatus
from Modulos_salvar import salvar_ativos, salvar_vulnerabilidade
from Modulos_adicionais import validador_int, validador_str





#------------------------ATUALIZAR CRUD-----------------------------#

def atualizar_crud(id=None):   #Atualiza os ativos, do menu ou na hora da leitura
    
    campo = {          #Campo de opções para atualização
1 : "Nome",
2 : "Descrição",
3 : "Responsável",
4 : "Setor",
5 : "Localização",
6 : "Tipo",
7 : "Vulnerabilidades",
8 : "Voltar ao menu"
}
    
    if not ativos_dicionario:
            print('NENHUM ATIVO CADASTRADO NO SISTEMA!')
            return
            
    if id is None:          #Coloquei id is None, para caso o usuario tenha escolhido direto do menu a opção atualização (Esse if escolhe o id do ativo)
        for k, v in ativos_dicionario.items():
                print(f'[{k}] - {v["Nome"].lower().capitalize()}')

        while True:

            ler_escolha = input('Digite o ativo que deseja visualizar: ').strip().lower()

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
                    break


    for k, v in ativos_dicionario[id].items():    #Mostra o ativo escolhido
        if k == 'Tipo':
            print(f'{k} = {v.name.lower().capitalize()}')
        else:
            print(f'{k} = {v}')                



    while True:
        print('Campos para atualização: ')             #Mostra o campo de atualização
        for k, v in campo.items():
            print(f'[{k}] {v}')

        
        escolha_campo = validador_int('Digite o campo que deseje alterar: ')        #Escolhe o que vai alterar e as condições é onde muda
        while escolha_campo not in range(1, 9):
            print('DIGITE UMA OPÇÃO VÁLIDA!')
            escolha_campo = validador_int('Digite o campo que deseje alterar: ')
            


        if escolha_campo == 1:
            campo_nome = validador_str('Digite a alteração: ')
            ativos_dicionario[id][campo[escolha_campo]] = campo_nome

        
        elif escolha_campo == 2:
            campo_descricao = validador_str('Digite a alteração: ')
            ativos_dicionario[id][campo[escolha_campo]] = campo_descricao

        
        elif escolha_campo == 3:
            campo_responsavel = validador_str('Digite a alteração: ')
            ativos_dicionario[id][campo[escolha_campo]] = campo_responsavel


        elif escolha_campo == 4:
            campo_setor = validador_str('Digite a alteração: ')
            ativos_dicionario[id][campo[escolha_campo]] = campo_setor


        elif escolha_campo == 5:
            campo_localizacao = validador_str('Digite a alteração: ')
            ativos_dicionario[id][campo[escolha_campo]] = campo_localizacao


        elif escolha_campo == 6:
            for t in TipoAtivos:                    #Mostra os tipos de ativos e pede a escolha
                print(f'[{t.value}] = {t.name}')

            while True:
                escolha_tipo = validador_int(f'Digite a atualização do tipo: ')
                try:
                    tipo = TipoAtivos(escolha_tipo)
                    break
                except ValueError:
                    print('TIPO ESCOLHIDO INVÁLIDO, ESCOLHA UM TIPO DA LISTA!')


            ativos_dicionario[id][campo[escolha_campo]] = tipo


        elif escolha_campo == 7:
            atualizar_vulnerabilidade(id)


        else:
            return
        

        
        salvar_ativos()

        #Opções de continuação
        print('''Opções de continuação:
[1] Atualizar outra informação do ativo
[2] Atualizar vulnerabilidades do ativo
[3] Voltar ao menu
''')
        
        escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')

        while escolha_continuacao not in range(1, 4):
            print('ESCOLHA UMA OPÇÃO EXISTENTE!')
            escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')


        if escolha_continuacao == 1:
            continue


        elif escolha_continuacao == 2:
            atualizar_vulnerabilidade(id)
            

        else:
            return


    


#------------------------ATUALIZAR VULNERABILIDADE-----------------------------#


def atualizar_vulnerabilidade(id=None):      #Atualiza as vulnerabilidades, pela opção de atualização ou na hora da leitura


    if not ativos_dicionario:
            print('NENHUM ATIVO CADASTRADO NO SISTEMA!')
            return
    
    
    if id is None:
            for k, v in ativos_dicionario.items():
                print(f'{k} = {v["Nome"]}')

            while True:
                # Escolha do ativo com tratamento try e except para aceitar id ou nome
                atualizar_crud_escolha = input('Digite o ativo que deseja atualizar a vulnerabilidade: ').strip().lower()

                try:
                    id = int(atualizar_crud_escolha)

                    if id not in ativos_dicionario:
                        print('DIGITE UM ID VÁLIDO!')
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
                        print(f'DIGITE UM NOME VÁLIDO!')
                        continue
                    break

    if id not in vulnerabilidades_dicionario or not vulnerabilidades_dicionario[id]:
        print('ESTE ATIVO NÃO POSSUI VULNERABILIDADES REGISTRADAS!')
        return

    campo_vuln = {                      #Campo de vulnerabilidade de opções para atualização
1 : "Vulnerabilidade",
2 : "Risco",
3 : "Categoria",
4 : "Severidade",
5 : "Status",
6 : "Voltar ao menu"
}

    while True:
        for i, vuln in enumerate(vulnerabilidades_dicionario[id], start=1):  #Mostra as vulnerabilidades para escolha, como é uma lista, colocoquei o enumarate para enumerar ela e começar do 1
            print(f'[{i}] {vuln["Vulnerabilidade"]}')


        escolha_vuln = validador_int('Escolha a vulnerabilidade que deseja alterar: ')  #Escolha da vulnerabilidade
        while escolha_vuln < 1 or escolha_vuln > len(vulnerabilidades_dicionario[id]):
            print('ESCOLHA UMA OPÇÃO VÁLIDA!')
            escolha_vuln = validador_int('Escolha a vulnerabilidade que deseja alterar: ')

        vuln_escolhida = vulnerabilidades_dicionario[id][escolha_vuln - 1]   #Diminui 1 para compatilidade com a lista

        print('Campos para atualização: ')      #Mostra o campo de atualização
        for k, v in campo_vuln.items():
            print(f'[{k}] {v}')

        escolha_campo_vuln = validador_int('Digite o campo que deseje alterar: ')   # #Escolhe o que vai alterar e as condições é onde muda
        while escolha_campo_vuln not in range(1, 7):
            print('DIGITE UMA OPÇÃO VÁLIDA!')
            escolha_campo_vuln = validador_int('Digite o campo que deseje alterar: ')



        if escolha_campo_vuln == 1:
            campo_vulnerabilidade = validador_str('Digite a alteração: ')
            vuln_escolhida[campo_vuln[escolha_campo_vuln]] = campo_vulnerabilidade


        elif escolha_campo_vuln == 2:
            campo_risco = validador_str('Digite a alteração: ')
            vuln_escolhida[campo_vuln[escolha_campo_vuln]] = campo_risco


        elif escolha_campo_vuln == 3:
            campo_categoria = validador_str('Digite a alteração: ')
            vuln_escolhida[campo_vuln[escolha_campo_vuln]] = campo_categoria


        elif escolha_campo_vuln == 4:
            for s in TipoSeveridade:                    #Mostra as severidades e pede a atualização
                print(f'[{s.value}] = {s.name}')

            while True:
                escolha_severidade = validador_int(f'Digite a atualização da severidade: ')
                try:
                    severidade = TipoSeveridade(escolha_severidade)
                    break
                except ValueError:
                    print('SEVERIDADE ESCOLHIDA É INVÁLIDA, ESCOLHA UMA SEVERIDADE DA LISTA!')

            vuln_escolhida[campo_vuln[escolha_campo_vuln]] = severidade


        elif escolha_campo_vuln == 5:
            for st in TipoStatus:                    #Mostra os tipos de ativos e pede a escolha
                print(f'[{st.value}] = {st.name}')

            while True:
                escolha_status = validador_int(f'Digite a atualização do status: ')
                try:
                    status = TipoStatus(escolha_status)
                    break
                except ValueError:
                    print('STATUS ESCOLHIDO É INVÁLIDO, ESCOLHA UM STATUS DA LISTA!')

            vuln_escolhida[campo_vuln[escolha_campo_vuln]] = status


        else:
            return


        salvar_vulnerabilidade()


        #Opções de continuação
        print('''Opções de continuação:

        [1] Atualizar outra vulnerabilidade
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