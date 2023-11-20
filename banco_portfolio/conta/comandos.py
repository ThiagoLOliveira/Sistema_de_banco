import mysql.connector

def depositar(id, valor):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="banco"
        )
    try:
        #Adicionar o ID do cliente que ira depositar 
        cursor = conn.cursor()
        deposito = "INSERT INTO extratos (id_cliente, valor) VALUES (%s, %s)"
        valores_deposito = (id, valor)
        cursor.execute(deposito, valores_deposito)
        conn.commit()
        print('Valor depositado com Sucesso')
    except Exception as e:
        print(f'Erro 2 Ocorreu algum erro {e}. Por favor, tente novamente mais tarde!.')
    finally:
        conn.close()
        cursor.close()