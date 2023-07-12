def view(query, campo="", filtro=""):

    import mysql.connector
    import pandas

    diretorio_download = 'C:/'
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
        sn = str(input('Deseja incluir algum filtro? [S/N]: ')).upper().strip()
        if sn == 'S':
            campo = input('Campo: ')
            filtro = input('Filtro: ')

        if campo == "":
            sql = f'SELECT * FROM {query};'
        else:
            sql = f'SELECT * FROM {query} WHERE {campo} like "%{filtro}";'
        print(sql)
        cursor.execute(sql)
        colunas = [column[0] for column in cursor.description]
        cabecalho_formatado = [coluna for coluna in colunas]
        print('| '.join(cabecalho_formatado))
        for row in cursor.fetchall():
            linha_formatada = [str(valor) for valor in row]
            print(f'| '.join(linha_formatada))

        sn = str(input(f'Gostaria de fazer download dessa view? [S/N] ')).upper().strip()
        if sn == 'S':
            cursor.execute(sql)
            # Criar um DataFrame pandas com os resultados
            df = pandas.DataFrame(cursor.fetchall(), columns=cursor.description)

            # Salvar o DataFrame em um arquivo CSV
            df.to_csv(f'{diretorio_download}', index=True)

        # Encerrando conexão
        if conect.is_connected():
            cursor.close()
            conect.close()
            input('Próxima query?!')


def personalizado(query):

    import mysql.connector
    import pandas

    diretorio_download = 'F:/Leonardo/Documents/AppFinanceiro/downloads'
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

        sn = str(input(f'Gostaria de fazer download dessa view? [S/N] ')).upper().strip()
        if sn == 'S':
            cursor.execute(sql)

            # Criar um DataFrame pandas com os resultados
            df = pandas.DataFrame(cursor.fetchall(), columns=cursor.description)

            # Salvar o DataFrame em um arquivo CSV
            df.to_csv(f'{diretorio_download}', index=False)

        # Encerrando conexão
        if conect.is_connected():
            cursor.close()
            conect.close()
            print('Próxima query?!')
