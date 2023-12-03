import mysql.connector

def chave():
# Conecte-se ao banco de dados
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="banco"
    )

    # Crie um cursor para executar comandos SQL
    cursor = conn.cursor()
    try: 
        metodo = int(input('Deseja entrar via CPF[1] ou CONTA[2] '))
        id = 0
        if metodo == 1:
            cpf = input('Insira seu CPF: ')
            entrada1 = "SELECT id FROM cadastro WHERE cpf = %s"
            cursor.execute(entrada1, (cpf,))
            resultado = cursor.fetchall()
            for i in resultado:
                for t in i:
                    id = t
        if metodo == 2:
            conta = input('Insira sua CONTA: ')
            entrada1 = "SELECT id FROM conta WHERE conta = %s"
            cursor.execute(entrada1, (conta,))
            resultado = cursor.fetchall()
            for i in resultado:
                for t in i:
                    id = t
    except mysql.connector.Error as e:
        print(f'Ocorreu um erro: {e}')
    finally:
        if conn is not None:
            conn.close()
        if cursor is not None:
            cursor.close()
    return id


def entrada(id):
    flag = False
    # Conecte-se ao banco de dados
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="banco"
    )

    # Crie um cursor para executar comandos SQL
    cursor = conn.cursor()
    try:
        identificador = id
        entrada = "SELECT id FROM segurança WHERE id = %s"
        cursor.execute(entrada, (identificador,))
        results = cursor.fetchall()
        if cursor.rowcount == '' :
            senha = input('Crie uma senha: ').strip()
            sql_senha = "INSERT INTO segurança (senha) VALUES (%s)"
            cursor.execute(sql_senha, (senha,))
            conn.commit()
        else:
            entrar = input('Insira sua senha: ').strip()
            digs_senha = []
            for i in entrar:
                digs_senha.append(i)
            entrada_senha = ''.join(digs_senha)
            sql_verificar_senha = "SELECT senha FROM segurança WHERE id = %s"
            cursor.execute(sql_verificar_senha, (identificador,))
            senha_armazenada = cursor.fetchone()
            senha_entrada = []
            for i in senha_armazenada:
                senha_entrada.append(i)
            verifica_senha = ''.join(senha_entrada)
            if entrada_senha == verifica_senha:
                flag = True
            else:
                print('Senha incorreta')
    except Exception as e:
        print(f'Ocorreu o seguinte erro: {e}')
    finally:
        if conn:
            conn.close()
        if cursor:
            cursor.close()
    if flag:
        return id
