def gasto(query):
    import mysql.connector

    host = 'lfmerukkeiac5y5w.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
    database = 'v608yl3l1m7nhv6w'
    user = 't6difi8xojnoqgpb'
    password = 'xp4e8b4itbdm96co'

    # Entrando com credenciais no MySQL
    conect = mysql.connector.connect(
        host=f'{host}',
        database=f'{database}',
        user=f'{user}',
        password=f'{password}')

    # Vrificando conexão ao MySQL
    if conect.is_connected():
        db_info = conect.get_server_info()
        print(f'Conectado a versâo do MySQL{db_info}')
        cursor = conect.cursor()
        cursor.execute('select database();')
        resp = cursor.fetchone()
        print(f'Conectado a {resp}')

    # Tranferir para o MySQL
    import datetime
    if query == "registrar_gasto":
        while True:

            movimentacao = str(input(f'Qual tipo de movimentação [Entrada/Saída]: ')).upper().strip()
            pagamento = str(input(f'Qual foi a forma de pagamento: ')).upper().strip()
            compra_paga = datetime.datetime.strptime(input('Data da movimentação: '), "%d/%m/%Y").date()

            if pagamento == 'DÉBITO' or 'DINHEIRO':
                vencimento = compra_realizada = compra_paga

            elif pagamento == 'CRÉDITO':
                compra_realizada = datetime.datetime.strptime(input('Data da Compra: '), "%d/%m/%Y").date()
                vencimento = datetime.datetime.strptime(input('Data do Vencimento: '), "%d/%m/%Y").date()

            else:
                break

            import AddRead

            valor = float(input(f'Qual o valor da movimentação: '))
            banco = str(input(f'Em qual banco ocorreu a movimentação: ')).upper().strip()

            AddRead.personalizado('SELECT tipo_desc FROM descricao ORDER BY tipo_desc')

            descricao = str(input(f'Qual descrição corresponde a essa movimentação: ')).upper().strip()

            AddRead.personalizado(f'''SELECT destinatario 
                                    FROM registro_fin 
                                    WHERE descricao = '{descricao}' 
                                    GROUP BY destinatario
                                    ORDER BY descricao''')

            destinatario = str(input(f'Quem foi o destinatário e/ou remetente: ')).upper().strip()
            observacao = str(input(f'Alguma observação sobre essa movimentação: ')).upper().strip()

            sql = f'''CALL registrar_gasto (
            "{compra_realizada}",
            "{vencimento}",
            "{compra_paga}",
            "{descricao}",
            "{valor}",
            "{movimentacao}",
            "{banco}",
            "{destinatario}",
            "{observacao}",
            "{pagamento}");'''

            print(sql)

            cursor = conect.cursor()
            cursor.execute(sql)
            conect.commit()

            break

    elif query == "registrar_gasto_parcelado":
        while True:

            movimentacao = str(input(f'Qual tipo de movimentação [Entrada/Saída]: ')).upper().strip()
            pagamento = str(input(f'Qual foi a forma de pagamento: ')).upper().strip()
            compra_realizada = datetime.datetime.strptime(input('Data da Compra: '), "%d/%m/%Y").date()
            vencimento = datetime.datetime.strptime(input('Data do 1º Vencimento: '), "%d/%m/%Y").date()
            parcelas = int(input(f'Qual o número de parcelas: '))
            valor = float(input(f'Qual o valor da movimentação: '))
            banco = str(input(f'Em qual banco ocorreu a movimentação: ')).upper().strip()

            import AddRead
            from dateutil.relativedelta import relativedelta

            AddRead.personalizado('''SELECT tipo_desc 
                                    FROM descricao 
                                    WHERE status = "ATIVO"
                                    ORDER BY tipo_desc''')

            descricao = str(input(f'Qual descrição corresponde a essa movimentação: ')).upper().strip()

            AddRead.personalizado(f'''SELECT destinatario 
                                    FROM registro_fin 
                                    WHERE descricao = '{descricao}' 
                                    GROUP BY destinatario
                                    ORDER BY descricao''')

            destinatario = str(input(f'Quem foi o destinatário e/ou remetente: ')).upper().strip()
            observacao = str(input(f'Alguma observação sobre essa movimentação: ')).upper().strip()

            for parcelas in range(0, parcelas):
                vencimento = vencimento + relativedelta(months=parcelas)
                sql = f'''CALL registrar_gasto_parcelado (
                  "{compra_realizada}",
                  "{vencimento}",
                  "{descricao}",
                  "{valor}",
                  "{movimentacao}",
                  "{banco}",
                  "{destinatario}",
                  "{observacao}",
                  "{pagamento}");'''

                print(sql)

                sn = str(input(f'Deseja inserir esses dados no banco? [S/N]: ')).upper().strip()
                if sn == 'S':
                    cursor = conect.cursor()
                    cursor.execute(sql)
                    conect.commit()

    elif query == "efetuar_pagamento":
        while True:

            idl = int(input(f'Qual o ID da conta que deseja pagar? '))
            pagamento = str(input(f'Confirme a forma de pagamento: ')).upper().strip()
            compra_paga = datetime.datetime.strptime(input('Data do pagamento: '), "%d/%m/%Y").date()
            valor = float(input(f'Qual o valor da movimentação: '))
            banco = str(input(f'Em qual banco ocorreu a movimentação: ')).upper().strip()
            observacao = str(input(f'Alguma observação sobre essa movimentação: ')).upper().strip()
            sql = f'''CALL efetuar_pagamento (
                  "{idl}",
                  "{compra_paga}",
                  "{valor}",
                  "{banco}",
                  "{observacao}",
                  "{pagamento}");'''

            print(sql)

            sn = str(input(f'Deseja inserir esses dados no banco? [S/N]: ')).upper().strip()
            if sn == 'S':
                cursor = conect.cursor()
                cursor.execute(sql)
                conect.commit()

    elif query == "transferencia":
        while True:

            compra_paga = datetime.datetime.strptime(input('Data da movimentação: '), "%d/%m/%Y").date()
            valor = float(input(f'Qual o valor da movimentação: '))
            banco1 = str(input(f'Banco de saída: ')).upper().strip()
            banco2 = str(input(f'Banco de entrada: ')).upper().strip()
            observacao = str(input(f'Alguma observação sobre essa movimentação: ')).upper().strip()
            sql = f'''CALL transferencia (
                  "{compra_paga}",
                  "{valor}",
                  "{banco1}",
                  "{banco2}",
                  "{observacao}");'''

            print(sql)

            sn = str(input(f'Deseja inserir esses dados no banco? [S/N]: ')).upper().strip()
            if sn == 'S':
                cursor = conect.cursor()
                cursor.execute(sql)
                conect.commit()

    else:
        print(f'Query não encontrada')

    # Encerrando conexão
    if conect.is_connected():
        cursor = conect.cursor()
        cursor.close()
        conect.close()


def tables():
    import mysql.connector

    host = 'lfmerukkeiac5y5w.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
    database = 'v608yl3l1m7nhv6w'
    user = 't6difi8xojnoqgpb'
    password = 'xp4e8b4itbdm96co'

    # Entrando com credenciais no MySQL
    conect = mysql.connector.connect(
        host=f'{host}',
        database=f'{database}',
        user=f'{user}',
        password=f'{password}')

    # Vrificando conexão ao MySQL
    if conect.is_connected():
        db_info = conect.get_server_info()
        print(f'Conectado a versâo do MySQL{db_info}')
        cursor = conect.cursor()
        cursor.execute('select database();')
        resp = cursor.fetchone()
        print(f'Conectado a {resp}')

    print('Opção ainda não implantada')
    import AddRead

    AddRead.personalizado('SHOW TABLES')

    tb = str(input(f'Qual tabela quer alterar: ')).upper().strip()
    ia = str(input(f'Deseja alterar ou inserir dados: ')).upper().strip()
    nome = str(input(f'Qual o nome do campo: ')).upper().strip()

    if ia == 'I' or 'INSERIR':
        sql = f'''CALL inserir_{tb} (
                "{nome}");'''

        print(sql)

    elif ia == 'A' or 'ALTERAR':
        ident = int(input(f'Qual o id: '))
        sql = f'''CALL alterar_{tb} (
                "{ident}");'''

        print(sql)

    # Encerrando conexão
    if conect.is_connected():
        cursor = conect.cursor()
        cursor.close()
        conect.close()
