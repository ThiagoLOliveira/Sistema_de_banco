# Cadastro de Clientes:

# Criação de contas bancárias para clientes.
# Armazenamento de informações pessoais, como nome, endereço, CPF, etc.
# Verificação da autenticidade dos dados do cliente.
def gera_cadastro():
    import mysql.connector
    from verifica_cpf import validaCpf
    from conta import tipo_conta, conta


    #Receber o nome do cliente
    def nome_cliente():
        while True:
            try:
                nome = str(input('Insira seu nome: ')).strip()
                resp = str(input('Deseja salvar esse nome? So podera trocar apos analise do departamento![Sim/Não] ' )).upper().strip()
                if resp == 'sim':
                    return nome.capitalize()
            except Exception as e:
                print(f'Erro ao inserir dado: {e}')

    # Recber o email do cliente
    def email_cliente():
        while True:
            try:
                email = str(input('Insira seu email: ')).strip()
                resp = str(input('Confirmar envio do email? [S/N] ' )).upper().strip()
                if resp == 'sim':
                    return email
            except Exception as e:
                print(f'Erro ao inserir dado: {e}')

    # Pede o valor de RG, sendo um valor valido, sem digitos, flag vira True    
    def rg_cliente():
        flag = False
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
        """Funçãp que recebera o CPF (Certificado Pessoa Fisica) do cliente

        Returns:
            Lista: Retorna somente se o valor informado for um CPF valido, caso contrario o sistema ira pedir novamente o Dado.
        """        
        lista_cpf = []
        while len(lista_cpf) < 11:
            lista_cpf.clear()
            # Usa a função do verifica_cpf e valida o cpf
            try:
                cpf = input('Digite seu cpf: ').strip()
                resultado = validaCpf(cpf)
                if resultado is True:
                    lista_cpf.append(cpf)
                    break
            except Exception as e:
                print(f'Erro ao inserir dado: {e}')
        return lista_cpf

    # Função que guarda o CEP em uma lista
    def cep_cliente():
        """Função que recebe o Codigo de endereço Postal (CEP) do cliente e armazena em uma lista

        Returns:
            _Cep_: Retorna uma lista.
        """        
        lista_cep = []
        while len(lista_cep) < 8:
            lista_cep.clear()
            try:
                cep = input('Insira seu CEP: ').strip()
                for i in cep:
                    lista_cep.append(i)
            except Exception as e:
                print(f'Erro ao inserir dado: {e}')
        return lista_cep

    def telefone_cliente():
        lista = []
        try:
            while True:
                telefone = int(input('Insira seu telefone: '))
                if type(telefone) != int:
                    telefone = int(input('Insira seu telefone: '))
                else:
                    for i in telefone:
                        lista.append(str(i))
        except Exception as e:
            print(f'Ocorreu o seguinte erro: {e}')
        return lista
    
    nome = nome_cliente()
    email = email_cliente()
    rg = rg_cliente()
    cpf = cpf_cliente()
    cep = cep_cliente()
    telefone = telefone_cliente()
    tipo_da_conta = tipo_conta()
    conta_nova, dig_conta = conta()

    cpf_str = ''.join(cpf)
    rg_str = ''.join(rg)
    cep_str = ''.join(cep)
    telefone_str = ''.join(telefone)
    
    def inserir_dados_cliente(nome, cpf, rg, email, cep, tipo_da_conta, conta, dig_conta, telefone_str):
        """ Puxara todos os dados fornecidos e encaminhara para o banco de dados pre-determinado, armazenando-os. Nenhum valor pode ser Nulo
        

        Args:
            nome (_str_): _Nome completo do cliente.
            cpf (_int_): _CPF (Certifcado Pessoa Fisica) do cliente, CPF`s invalidos serão automaticamentes recusado pelo sistema.
            rg (_int_): _RG (Registro Geral) do cliente.
            email (_str_): _Email para envio de dados.
            cep (_int_): _CEP (Codigo de endereço Postal) localização onde mora o cliente.
            conta (_int_): _Conta gerada a partir de regras pre-determinadas.
            tipo_conta (_int_): _So tem duas entrada 013 para conta Poupança ou 001 para conta Corrente .
        """        
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
            sql_base_conta = "INSERT INTO cadastro (nome, cpf, rg, email, cep, telefone) VALUES (%s, %s, %s, %s, %s, %s)"
            sql = "INSERT INTO conta (conta, digito_conta, tipo_conta) VALUES (%s, %s, %s)"

            # Valores a serem inseridos
            valores_base_conta = (nome, cpf, rg, email, cep, telefone_str)
            valores = (conta, dig_conta, tipo_da_conta)
            
            # Execute a consulta SQL
            cursor.execute(sql_base_conta, valores_base_conta)
            cursor.execute(sql, valores)
            
            # Faça o commit para salvar as alterações no banco de dados
            conn.commit()
            
            # Feche o cursor e a conexão
            cursor.close()
            conn.close()

            print("Dados do cliente inseridos com sucesso!")
            print(telefone)
        except mysql.connector.Error as e:
            print(f"Erro ao inserir dados do cliente: {e}")
            print(telefone)
            
    inserir_dados_cliente(nome, cpf_str, rg_str, email, cep_str, tipo_da_conta, conta_nova, dig_conta, telefone_str)