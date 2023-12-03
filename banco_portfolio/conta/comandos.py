import mysql.connector


def pega_dados(id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="banco"
    )
    try:
        cursor = conn.cursor()
        #pega o nome do cliente
        nome = f'SELECT nome FROM cadastro WHERE id = {id}'
        valores = f'SELECT sum(valor) as saldo_total FROM extratos WHERE id_cliente = {id}'
        
        cursor.execute(nome)
        nome_resultado = cursor.fetchone()
        
        #pega o saldo total do cliente
        cursor.execute(valores)
        saldo_total = cursor.fetchone()
        
        nome = nome_resultado[0]
        saldo = saldo_total[0]
        
        print(f"Olá {nome}, seja bem vindo(a) \n")
        print(f'Seu saldo atual é de {saldo}')
    except Exception as e:
        print(f'Ocorreu um erro {e}, tente novamente mais tarde!.')
    finally:
        cursor.close()
        conn.close()
    


def depositar(id, valor, tipo):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="banco"
        )
    try:
        #Adicionar o ID do cliente que ira depositar 
        cursor = conn.cursor()
        deposito = "INSERT INTO extratos (id_cliente, valor, tipo) VALUES (%s, %s, %s)"
        valores_deposito = (id, valor, tipo)
        cursor.execute(deposito, valores_deposito)
        conn.commit()
        print('Valor depositado com Sucesso')
    except Exception as e:
        print(f'Erro 2 Ocorreu algum erro {e}. Por favor, tente novamente mais tarde!.')


def saque(id):
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="banco"
        )
        try:
            cursor = conn.cursor()
            cursor.execute()
        except Exception as e:
            print(f'Ocorreu um erro {e}')
        finally:
            cursor.close()
            conn.close()