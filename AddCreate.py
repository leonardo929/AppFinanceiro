def backup():

    import pandas
    import mysql.connector

    diretorio_backup = 'F:/Leonardo/Documents/AppFinanceiro/downloads'
    host = 'lfmerukkeiac5y5w.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
    database = 'v608yl3l1m7nhv6w'
    user = 't6difi8xojnoqgpb'
    password = 'xp4e8b4itbdm96co'
    querys = ['banco', 'categoria', 'descricao', 'grupo', 'movimentacao', 'pagamento', 'registro_fin']

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
        for query in querys:
            sql = f'SELECT * FROM {query};'
            cursor.execute(sql)

            # Criar um DataFrame pandas com os resultados
            df = pandas.DataFrame(cursor.fetchall(), columns=cursor.description)

            # Salvar o DataFrame em um arquivo CSV
            df.to_csv(f'{diretorio_backup}', index=False)

        # Encerrando conexão
        if conect.is_connected():
            cursor.close()
            conect.close()
            input('Próxima query?!')

    print(f'O backup foi criado em: {diretorio_backup}')


def personalizado(query):

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
        print(f'Conectado a versão do MySQL{db_info}')
        cursor = conect.cursor()
        cursor.execute('select database();')
        resp = cursor.fetchone()
        print(f'Conectado a {resp}')

        # Tranferir para o MySQL
        sql = f'{query};'
        print(sql)
        cursor.execute(sql)
        colunas = [column[0] for column in cursor.description]
        cabecalho_formatado = [coluna for coluna in colunas]
        print('| '.join(cabecalho_formatado))
        for row in cursor.fetchall():
            # print(f'{row}')
            linha_formatada = [str(valor) for valor in row]
            print(f'| '.join(linha_formatada))

        # Encerrando conexão
        if conect.is_connected():
            cursor.close()
            conect.close()
            print('Próxima query?!')


def schemas():

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
        print(f'Conectado a versão do MySQL{db_info}')
        cursor = conect.cursor()
        cursor.execute('select database();')
        resp = cursor.fetchone()
        print(f'Conectado a {resp}')

        # Execute uma consulta para recuperar as informações do banco de dados
        cursor.execute("SHOW TABLES;")

        # Recupere os nomes das tabelas
        tabelas = [str(tabela[0]) for tabela in cursor.fetchall()]
        print(f'| '.join(tabelas))

        # Encerrando conexão
        if conect.is_connected():
            cursor.close()
            conect.close()
            print('Próxima query?!')
