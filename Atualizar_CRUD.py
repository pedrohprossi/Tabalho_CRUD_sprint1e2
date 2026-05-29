from Ativos import ativos_dicionario, TipoAtivos, vulnerabilidades_dicionario, TipoSeveridade, TipoStatus
from Modulos_salvar import salvar_ativos, carregar_ativos, salvar_vulnerabilidade, carregar_vulnerabilidade
from Modulos_adicionais import validador_int, validador_str





#------------------------ATUALIZAR CRUD-----------------------------#

def atualizar_crud(id=None):
    
    campo = {
1 : "Nome",
2 : "Descrição",
3 : "Responsável",
4 : "Setor",
5 : "Localização",
6 : "Tipo",
7 : "Vulnerabilidades",
8 : "Voltar ao menu"
}
    
    
    if id is None:
        for k, v in ativos_dicionario.items():
                print(f'[{k}] - {v["Nome"].lower().capitalize()}')

        while True:

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


    for k, v in ativos_dicionario[id].items():
        if k == 'Tipo':
            print(f'{k} = {v.name.lower().capitalize()}')
        else:
            print(f'{k} = {v}')                



    while True:
        print('Campos para atualização: ')
        for k, v in campo.items():
            print(f'[{k}] {v}')

        
        escolha_campo = validador_int('Digite o campo que deseje alterar: ')
        while escolha_campo not in range(1, 8):
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
                escolha_tipo = validador_int(f'Digite o tipo do novo ativo: ')
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


        print('''Opções de continuação:
[1] Atualizar outra informação do ativo
[2] Atualizar vulnerabilidades do ativo
[3] Voltar ao menu
''')
        
        escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')

        while escolha_continuacao not in range(1, 5):

            print('ESCOLHA UMA OPÇÃO EXISTENTE!')
            print('''Opções de continuação:
[1] Atualizar ativo
[2] Ler vulnerabilidades do ativo
[3] Ler outro ativo
[4] Voltar ao menu
''')
            escolha_continuacao = validador_int('Digite a opção que deseja efetuar: ')

        if escolha_continuacao == 1:
            continue


        elif escolha_continuacao == 2:
            atualizar_vulnerabilidade(id)
            

        else:
            return


    


#------------------------ATUALIZAR VULNERABILIDADE-----------------------------#


def atualizar_vulnerabilidade(id):
    