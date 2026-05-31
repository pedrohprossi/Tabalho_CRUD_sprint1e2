from Ativos import ativos_dicionario, vulnerabilidades_dicionario
from Modulos_salvar import carregar_ativos, carregar_vulnerabilidade
from Modulos_adicionais import validador_int, validador_str
from Criar_CRUD import criar_crud, adicionar_vulnerabilidade
from Ler_CRUD import ler_crud, ler_vulnerabilidade
from Atualizar_CRUD import atualizar_crud, atualizar_vulnerabilidade
from Deletar_CRUD import deletar_crud, deletar_vulnerabilidade


#-------------------MENU--------------------#


ativos_dicionario.update(carregar_ativos())
vulnerabilidades_dicionario.update(carregar_vulnerabilidade())

while True:
    


    print('''[1] Cadastrar 
    [2] Ler
    [3] Atualizar 
    [4] Deletar 
    [5] Sair do programa
    ''')

    escolha_menu = validador_int('Digite a ação que deseja executar no programa:')
    while escolha_menu not in range(1, 6):
        print('ESCOLHA UMA OPÇÃO VÁLIDA!')
        escolha_menu = validador_int('Digite a ação que deseja executar no programa:')

    
    if escolha_menu == 1:
        print('''[1] Cadastrar um ativo
[2] Cadastrar uma vulnerabilidade
''')
        escolha_cadastrar = validador_int('Digite o que deseja cadastrar: ')
        while escolha_cadastrar not in (1, 2):
            print('ESCOLHA UMA OPÇÃO VÁLIDA!')
            escolha_cadastrar = validador_int('Digite o que deseja cadastrar: ')
        
        if escolha_cadastrar == 1:
            criar_crud()
        else:
            adicionar_vulnerabilidade(id=None)

    

    elif escolha_menu == 2:
        print('''[1] Ler um ativo
[2] Ler uma vulnerabilidade
''')
        escolha_ler = validador_int('Digite o que deseja ler: ')
        while escolha_ler not in (1, 2):
            print('ESCOLHA UMA OPÇÃO VÁLIDA!')
            escolha_ler = validador_int('Digite o que deseja ler: ')
        
        if escolha_ler == 1:
            ler_crud()
        else:
            ler_vulnerabilidade(id=None)

    

    elif escolha_menu == 3:
        print('''[1] Atualizar um ativo
[2] Atualizar uma vulnerabilidade
''')
        escolha_atualizar = validador_int('Digite o que deseja atualizar: ')
        while escolha_atualizar not in (1, 2):
            print('ESCOLHA UMA OPÇÃO VÁLIDA!')
            escolha_atualizar = validador_int('Digite o que deseja atualizar: ')
        
        if escolha_atualizar == 1:
            atualizar_crud()
        else:
            atualizar_vulnerabilidade(id=None)
    


    elif escolha_menu == 4:
        print('''[1] Deletar um ativo
[2] Deletar uma vulnerabilidade
''')
        escolha_deletar = validador_int('Digite o que deseja deletar: ')
        while escolha_deletar not in (1, 2):
            print('ESCOLHA UMA OPÇÃO VÁLIDA!')
            escolha_deletar = validador_int('Digite o que deseja deletar: ')
    
        if escolha_deletar == 1:
            deletar_crud()
        else:
            deletar_vulnerabilidade(id=None)
    


    else:
        break
        



