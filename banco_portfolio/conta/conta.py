# Cadastro de Clientes:

# Criação de contas bancárias para clientes.
# Armazenamento de informações pessoais, como nome, endereço, CPF, etc.
# Verificação da autenticidade dos dados do cliente.

import mysql.connector
from verifica_cpf import validaCpf


#Receber o nome do cliente
def nome_cliente():
    while True:
        try:
            nome = str(input('Insira seu nome: '))
            resp = str(input('Deseja salvar esse nome? So podera trocar apos analise do departamento![S/N] ' )).upper()
            if resp in 'SsSimsimSIM':
                return nome.capitalize()
        except Exception as e:
            print(f'Erro ao inserir dado: {e}')

# Recber o email do cliente
def email_cliente():
    while True:
        try:
            email = str(input('Insira seu email: '))
            resp = str(input('Confirmar envio do email? [S/N] ' )).upper()
            if resp in 'SsSimsimSIM':
                return email
        except Exception as e:
            print(f'Erro ao inserir dado: {e}')

# Pede o valor de RG, sendo um valor valido, sem digitos, flag vira True    
def rg_cliente():
    flag = False
    rg_str = ''
    while flag != True:
        try:
            rg = input('Digite seu RG, sem o digito verificador: ').strip() # Elimina os espaços caso o cliente venha a colocar
            lista = list(rg)
            # for i in lista:
            #     lista_rg.append(int(i))
            if len(lista) < 7:
                while flag != True:
                    try:
                        lista.clear()
                        rg = input('Digite os digitos exatos, sem o verificador!: ').strip()
                        lista1 = list(rg)
                        for i in lista1:
                            lista.append(str(i))
                        if len(lista) == 8:
                            flag = True
                    except:
                        print('Digite valores validos')
        except Exception as e:
            print(f'Erro ao inserir dado: {e}')
        else:
            break
    return lista

# Função que armazena o CPF em uma lista
def cpf_cliente():
    lista_cpf = []
    while len(lista_cpf) < 11:
        lista_cpf.clear()
        # Usa a função do verifica_cpf e valida o cpf
        try:
            cpf = input('Digite seu cpf: ')
            resultado = validaCpf(cpf)
            if resultado is True:
                lista_cpf.append(cpf)
                break
        except Exception as e:
            print(f'Erro ao inserir dado: {e}')
    return lista_cpf

# Função que guarda o CEP em uma lista
def cep_cliente():
    lista_cep = []
    while len(lista_cep) < 8:
        lista_cep.clear()
        try:
            cep = input('Insira seu CEP: ')
            for i in cep:
                lista_cep.append(i)
        except Exception as e:
            print(f'Erro ao inserir dado: {e}')
    return lista_cep


nome = nome_cliente()
email = email_cliente()
rg = rg_cliente()
cpf = cpf_cliente()
cep = cep_cliente()


cpf_str = ''.join(cpf)
rg_str = ''.join(rg)
cep_str = ''.join(cep)


def inserir_cliente(nome, cpf, rg, email, cep):
    try:
        # Conecte-se ao banco de dados
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="banco"
        )

        # Crie um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Defina a consulta SQL para inserção de dados
        sql = "INSERT INTO usuario (nome, cpf, rg, email, cep) VALUES (%s, %s, %s, %s, %s)"

        # Valores a serem inseridos
        valores = (nome, cpf, rg, email, cep)

        # Execute a consulta SQL
        cursor.execute(sql, valores)

        # Faça o commit para salvar as alterações no banco de dados
        conn.commit()

        # Feche o cursor e a conexão
        cursor.close()
        conn.close()

        print("Dados do cliente inseridos com sucesso!")

    except mysql.connector.Error as e:
        print(f"Erro ao inserir dados do cliente: {e}")

inserir_cliente(nome, cpf_str, rg_str, email, cep_str)