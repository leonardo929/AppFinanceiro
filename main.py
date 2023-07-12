# Sistema Financeiro Python
print(''' Esse sistema deve ser usado para alimentação de dados e
   emição de relatórios no MySQL;
    Requisitos mínimos: MySQL 8.0, Python 3.9.10 ou superior
    Bibliotecas necessarias - mysql.connector - AddNovoCliente - ExibirView - AddCadProduto - AddEntradaProd - time
''')

# Abertura
user = 'leonardo.vieira'
senha = 'Vieira2002.'

while True:
    acessoUser = input('Usuário: ')
    if user == acessoUser:
        acessoSenha = input('Insira a Senha de acesso: ')
        if senha == acessoSenha:
            break
        else:
            print('Senha incorreta. Tente novamente!')
    else:
        print('Usuário não cadastrado. Tente novamente!')

print(f'\n===== Bem Vindo {user} =====\n')
print(f'===== Sistema Financeiro 1.2.0 =====')

# Menu
while True:
    try:

        selecaoMenu = int(input(
            '''   
            [1] - Create
            [2] - Read
            [3] - Update
            [9] - Sair
      
            Selecione uma opção - '''))

        # Navegação
        # Creat
        if selecaoMenu == 1:
            import AddCreate
            while True:
                try:

                    selecaoCreate = int(input(
                        '''   
                        [1] - Backup
                        [2] - Schemas
                        [3] - Personalizado
                        [99] - Voltar
            
                        Selecione uma opção - '''))

                    if selecaoCreate == 1:
                        AddCreate.backup()
                    elif selecaoCreate == 2:
                        AddCreate.schemas()
                    elif selecaoCreate == 3:
                        AddCreate.personalizado(input('Query: \n'))
                    elif selecaoCreate == 99:
                        break

                # Localizar Erro
                except Exception as erro:
                    print(f'Foi encontrado um erro de {erro}')

        # Read
        elif selecaoMenu == 2:
            import AddRead
            while True:
                try:

                    selecaoRead = int(input(
                        '''   
                        [1] - View Saldo Atual
                        [2] - View Últimos Registros
                        [3] - View Movimentação Mês
                        [4] - View Balanço Mês
                        [5] - View Analise de Categoria por Mês
                        [6] - View Analise de Descrição por Mês
                        [7] - View Credores / Devedores
                        [8] - View Analise
                        [9] - Personalizado
                        [10] - Dívidas Pendentes
                        [99] - Voltar
            
                        Selecione uma opção - '''))

                    if selecaoRead == 1:
                        AddRead.view('saldo_atual')
                    elif selecaoRead == 2:
                        AddRead.view('ultimos_registros')
                    elif selecaoRead == 3:
                        AddRead.view('movimentacao_mes')
                    elif selecaoRead == 4:
                        AddRead.view('balanco_mes')
                    elif selecaoRead == 5:
                        AddRead.view('categoria_mes')
                    elif selecaoRead == 6:
                        AddRead.view('descricao_mes')
                    elif selecaoRead == 7:
                        AddRead.view('credores_devedores')
                    elif selecaoRead == 8:
                        AddRead.view('analise')
                    elif selecaoRead == 9:
                        AddRead.personalizado(input('Query: \n'))
                    elif selecaoRead == 10:
                        AddRead.view('dividas_pendentes')
                        sn = str(input(f'Deseja efetuar pagamento? ')).upper().strip()
                        if sn == 'S':
                            AddUpdate.gasto('efetuar_pagamento')
                    elif selecaoRead == 99:
                        break

                # Localizar Erro
                except Exception as erro:
                    print(f'Foi encontrado um erro de {erro}')

        # Update
        elif selecaoMenu == 3:
            import AddUpdate
            while True:
                try:
                    
                    selecaoUpdate = int(input(
                        '''   
                        [1] - Inserir Movimentação Unica
                        [2] - Inserir Movimentação Fixa / Parcelada
                        [3] - Efetuar Pagamento
                        [4] - Efetuar Transferência
                        [5] - Alterar Gastos
                        [6] - Alterar Bancos
                        [7] - Alterar Categorias
                        [8] - Alterar Descrições
                        [99] - Voltar
            
                        Selecione uma opção - '''))

                    if selecaoUpdate == 1:
                        AddUpdate.gasto('registrar_gasto')
                    elif selecaoUpdate == 2:
                        AddUpdate.gasto('registrar_gasto_parcelado')
                    elif selecaoUpdate == 3:
                        AddUpdate.gasto('efetuar_pagamento')
                    elif selecaoUpdate == 4:
                        AddUpdate.gasto('transferencia')
                    elif selecaoUpdate == 5:
                        AddUpdate.tables()
                    elif selecaoUpdate == 6:
                        AddUpdate.tables()
                    elif selecaoUpdate == 7:
                        AddUpdate.tables()
                    elif selecaoUpdate == 8:
                        AddUpdate.tables()
                    elif selecaoUpdate == 99:
                        break

                # Localizar Erro
                except Exception as erro:
                    print(f'Foi encontrado um erro de {erro}')

        # Fechar Programa
        elif selecaoMenu == 9:
            import time
            print('===== Você optou por fechar o programa. Volte sempre! =====')
            time.sleep(3)
            break

    # Localizar Erro
    except Exception as erro:
        print(f'Foi encontrado um erro de {erro}')
