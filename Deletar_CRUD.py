from Ativos import ativos_dicionario, TipoAtivos, vulnerabilidades_dicionario, TipoSeveridade, TipoStatus
from Modulos_salvar import salvar_ativos, carregar_ativos, salvar_vulnerabilidade, carregar_vulnerabilidade
from Modulos_adicionais import validador_int, validador_str


#--------------DELETAR ATIVOS-----------------#

def deletar_crud():

    while True:

        for k, v in ativos_dicionario.items():
            print(f'{k} = {v["Nome"]}')

        while True:
            # Escolha do ativo com tratamento try e except para aceitar id ou nome
            deletar_escolha = input('Digite o ativo deseja deletar: ').strip().lower()

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




        print('Ativo escolhido:')
        for k, v in ativos_dicionario[id].items():  # Mostra o ativo
            if k == 'Tipo':
                print(f'{k} = {v.name.lower().capitalize()}')
            else:
                print(f'{k} = {v}')


        confirmacao_deletar = validador_str(f'Tem certeza que deseja deletar o ativo {ativos_dicionario[id]["Nome"]}? [S/N]').upper()
        while confirmacao_deletar not in ('S','N'):
            print('DIGITE UMA OPÇÃO VÁLIDA!')
            confirmacao_deletar = validador_str(f'Tem certeza que deseja deletar o ativo {ativos_dicionario[id]["Nome"]}? [S/N]').upper()


        if confirmacao_deletar == 'S':
            del ativos_dicionario[id]
            if id in vulnerabilidades_dicionario:
                del vulnerabilidades_dicionario[id]

            salvar_ativos()

        else:
            return





#--------------DELETAR VULNERABILIDADES-----------------#

def deletar_vulnerabilidade(id=None):

    while True:
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



        print('''Opções de remoção:
        [1] Apagar todas as vulnerabilidades do ativo
        [2] Apagar apenas uma vulnerabilidade do ativo    
        ''')
        escolha_remocao = validador_int('Digite a opção de remoção que deseja realizar: ')
        while escolha_remocao not in (1, 2):
            print('DIGITE UMA OPÇÃO VÁLIDA!')
            escolha_remocao = validador_int('Digite a opção de remoção que deseja realizar: ')

        if escolha_remocao == 1:

            print('Vulnerabilidades escolhidas: ')
            for i, vuln in enumerate(vulnerabilidades_dicionario[id], start=1):
                print(f'{i} = {vuln["Vulnerabilidade"]}')


            confirmacao_deletar_tudo = validador_str(f'Tem certeza que deseja deletar TODAS as vulnerabilidades acima? [S/N]').upper()
            while confirmacao_deletar_tudo not in ('S', 'N'):
                print('DIGITE UMA OPÇÃO VÁLIDA!')
                confirmacao_deletar_tudo = validador_str(f'Tem certeza que deseja deletar TODAS as vulnerabilidades acima? [S/N]').upper()

            if confirmacao_deletar_tudo == 'S':
                del vulnerabilidades_dicionario[id]
                salvar_vulnerabilidade()

            else:
                return




        else:
            for i, vuln in enumerate(vulnerabilidades_dicionario[id], start=1):
                print(f'{i} = {vuln["Vulnerabilidade"]}')


            while True:

                # Escolha da vulnerabilidade, funciona colocando a opção ou a vulnerabilidade
                deletar_escolha_vulnerabilidade = input('Escolha a vulnerabilidade que deseja deletar: ').lower().strip()

                try:
                    vn = int(deletar_escolha_vulnerabilidade)
                    if vn < 1 or vn > len(vulnerabilidades_dicionario[id]):
                            print('DIGITE UM ID VÁLIDO!')
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
                        print(f'DIGITE UMA VULNERABILIDADE VÁLIDA!')
                        continue


            vuln_escolhida = vulnerabilidades_dicionario[id][vn - 1]  # Diminui um para compatilidade com a lista

            print('Vulnerabilidade escolhida:')
            for k, v in vuln_escolhida.items():  # Mostra a vulnerabilidade
                if k == 'Severidade' or k == 'Status':
                    print(f'{k} = {v.name.lower().capitalize()}')
                else:
                    print(f'{k} = {v}')

            confirmacao_deletar = validador_str(f'Tem certeza que deseja deletar a vulnerabilidade {vuln_escolhida["Vulnerabilidade"]}? [S/N]').upper()
            while confirmacao_deletar not in ('S', 'N'):
                print('DIGITE UMA OPÇÃO VÁLIDA!')
                confirmacao_deletar = validador_str(f'Tem certeza que deseja deletar a vulnerabilidade {vuln_escolhida["Vulnerabilidade"]}? [S/N]').upper()

            if confirmacao_deletar == 'S':
                    vulnerabilidades_dicionario[id].pop(vn-1)
                    salvar_vulnerabilidade()

            else:
                return