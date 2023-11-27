import mysql.connector

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
    finally:
        conn.close()
        cursor.close()


def saque(id):
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="banco"
        )
        try:
            cursor = conn.cursor()
            valores = f'SELECT sum(valor) as saldo_total FROM extratos WHERE id_cliente = {id}'
            cursor.execute(valores)
            result = cursor.fetchone()
            if result:
                saldo_total = result[0]
                print(f"Saldo total para o ID {id}: {saldo_total}")
            else:
                print(f"Nenhum resultado encontrado para o ID {id}")
        except Exception as e:
            print(f'Ocorreu um erro {e}')
        finally:
            cursor.close()
            conn.close()