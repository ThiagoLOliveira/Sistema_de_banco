# A estrutura de um número de conta bancária pode incluir os seguintes elementos:
# Código do banco: Este é um número único que identifica o banco onde a conta foi criada.  Numero do PyBank 23
# Código da agência: Identifica a agência específica onde a conta foi criada. 1
# Número da conta: Este é um número exclusivo que identifica a conta específica de um cliente na agência. 7 digitos
# Dígitos de controle: Alguns números de conta podem incluir dígitos de verificação, 1
# que ajudam a garantir a integridade dos dados e detectar erros de digitação.
# Informações adicionais: Dependendo do banco e do país, pode haver informações adicionais, como um código de filial ou tipo de conta.
from random import randint
import shutil

def tipo_conta():
    try:
        modelo_conta_corrente = "\033[1;47m\033[1mBeneficios de uma Conta Corrente\033[0m\033[0m"
        modelo_conta_poupanca = "\033[1;47m\033[1mBeneficios de uma Conta Poupança\033[0m\033[0m"
        largura_terminal, _ = shutil.get_terminal_size()

        modelo_conta_corrente = modelo_conta_corrente.center(largura_terminal)
        modelo_conta_poupanca = modelo_conta_poupanca.center(largura_terminal)


        print()
        print(f'Tipos de conta disponiveis:')
        print('-' * largura_terminal)
        print(modelo_conta_corrente)
        print('-' * largura_terminal)
        print()
        print('\033[1;44m\033[1mNa Conta Corrente você tera esses beneficios:\033[0m\033[0m')
        print('\033[1;47m\033[1m1° Acesso Fácil aos Fundos:\033[0m\033[0m Uma conta corrente é projetada para facilitar o acesso aos seus fundos.\n'
            'Você pode fazer saques, transferências, pagamentos e depósitos facilmente.')
        print()
        print('\033[1;47m\033[1m2° Pagamentos e Transações:\033[0m\033[0m Uma conta corrente permite fazer pagamentos de contas, transferências bancárias e transações com cartão de débito\n'
            'É uma conta ideal para as despesas diárias.')
        print()
        print('\033[1;47m\033[1m3° Cheques:\033[0m\033[0m Muitas contas correntes permitem o uso de cheques, o que é útil para pagar contas e fazer compras.')
        print()
        print('\033[1;47m\033[1m4° Linhas de Crédito:\033[0m\033[0m Alguns bancos oferecem linhas de crédito vinculadas à conta corrente, que podem ser úteis em momentos de emergência.')
        print()
        print('\033[1;47m\033[1m5° Conveniência:\033[0m\033[0m Uma conta corrente geralmente oferece serviços bancários online e móveis para facilitar o gerenciamento de suas finanças.')
        print()
        print('\033[1;47m\033[1m6° Facilidade de Pagamento:\033[0m\033[0m Com uma conta corrente, você pode configurar débitos automáticos para pagamentos regulares,\ncomo contas de serviços públicos e empréstimos.')
        print()

        print('-' * largura_terminal)
        print(modelo_conta_poupanca)
        print('-' * largura_terminal)
        print('\033[1;44m\033[1mNa Conta Poupança você tera esses beneficios:\033[0m\033[0m')
        print('\033[1;47m\033[1m1° Juros:\033[0m\033[0m Uma conta poupança geralmente paga juros sobre o saldo mantido na conta. Isso permite que seu dinheiro cresça ao longo do tempo.')
        print()
        print('\033[1;47m\033[1m2° Economia de Curto Prazo:\033[0m\033[0m Contas poupança são ideais para economias de curto prazo, como para objetivos de curto prazo ou para criar um fundo de emergência.')
        print()
        print('\033[1;47m\033[1m3° Segurança:\033[0m\033[0m O dinheiro em uma conta poupança é geralmente considerado mais seguro do que manter grandes quantias de dinheiro em casa.')
        print()
        print('\033[1;47m\033[1m4° Reserva de Emergência:\033[0m\033[0m Uma conta poupança pode ser usada para criar uma reserva de emergência para situações inesperadas.')
        print()
        print('\033[1;47m\033[1m5°Acessibilidade:\033[0m\033[0m Os fundos em uma conta poupança geralmente são acessíveis quando você precisar deles, embora possa haver limites em saques em alguns casos.')
        print()
        print('\033[1;47m\033[1m6° Disciplina Financeira:\033[0m\033[0m Uma conta poupança ajuda a separar seu dinheiro de gastos diários, promovendo a disciplina financeira.')
        print()
        
        while True:
            tipo = input('Insira um tipo de conta? [CC/CP] ').strip().upper()
            if tipo == 'CC':
                return tipo
            elif tipo == 'CP':
                return tipo
            else:
                continue
    except Exception as e:
        print(f'Erro ao inserir dado: {e}')
    return tipo


def conta():
    lista = []
    cod_banco = '23'
    cod_agencia = '1'
    num_conta = str(randint(1000, 9999))
    dig_controle = str(randint(1, 9))
    lista.append(cod_banco)
    lista.append(cod_agencia)
    lista.append(num_conta)
    conta_banco = ''.join(lista)
    return conta_banco, dig_controle
