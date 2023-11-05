from cliente import gera_cadastro
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
            cpf = int(input('Insira seu CPF: '))
            entrada1 = "SELECT id FROM cadastro WHERE cpf = %s"
            cursor.execute(entrada1, (cpf,))
            resultado = cursor.fetchall()
            for i in resultado:
                for t in i:
                    id = t
            print(id)
        if metodo == 2:
            conta = int(input('Insira sua CONTA: '))
            entrada1 = "SELECT id FROM conta WHERE conta = %s"
            cursor.execute(entrada1, (conta,))
            resultado = cursor.fetchall()
            for i in resultado:
                for t in i:
                    id = t
            print(id)
    except mysql.connector.Error as e:
        print(f'Ocorreu um erro: {e}')
    finally:
        if conn is not None:
            conn.close()
        if cursor is not None:
            cursor.close()
    return id


def entrada(id):
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
        if cursor.rowcount == 0 :
            senha = input('Crie uma senha: ').strip()
            sql_senha = "INSERT INTO segurança (senha) VALUES (%s)"
            cursor.execute(sql_senha, (senha,))
            conn.commit()
        else:
            entrar = input('Insira sua senha: ').strip()
            sql_verificar_senha = "SELECT senha FROM segurança WHERE id = %s"
            cursor.execute(sql_verificar_senha, (identificador,))
            senha_armazenada = cursor.fetchone()[0]
            if entrar == senha_armazenada:
                print('Bem-vindo ao Banco')
            else:
                print('Senha incorreta')
    except Exception as e:
        print(f'Ocorreu o seguinte erro: {e}')
    finally:
        if conn:
            conn.close()
        if cursor:
            cursor.close()


try:
    resp = str(input('Você ja tem cadastro? [S/N]')).strip().upper()
    if resp in 'sSSimSIM':
        logar = chave()
        entrar = entrada(logar)
    else:
        novo_cliente = gera_cadastro()
except TypeError or KeyError or NameError as e:
    print(f'Dados com erro: {e}')
finally:
    print('Obrigado por usar o Banco Python')