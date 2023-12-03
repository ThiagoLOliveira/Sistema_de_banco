from principal import chave, entrada
from cliente import gera_cadastro
import comandos as cd

import shutil

try:
    while True:
        resp = str(input('Você ja tem cadastro? [Sim/Nao]')).strip()
        if resp == 'sim':
            logar = chave()
            entrar = entrada(logar)
            break
        elif resp == 'não':
            novo_cliente = gera_cadastro()
            break
        else:
            print('Digite um valor valido')
except Exception as e:
    print(f'Dados com erro: {e}')


boas_vindas = "\033[1;47m\033[1mOque você deseja fazer? \033[0m\033[0m"
largura_terminal, _ = shutil.get_terminal_size()

boas_vindas = boas_vindas.center(largura_terminal)

cd.pega_dados(logar)

print('-' * largura_terminal)
print(boas_vindas)
print('-' * largura_terminal)
print('[1] DEPOSITO BANCARIO')
print('[2] SAQUE DA CONTA')
print('[3] EXTRATO BANCARIO')


try:
    while True:
        func = int(input('Digite uma opção: '))
        if func > 3 or func < 1:
            print('Digite um valor valido!! ')
        else:
            if func == 1:
                while True:
                    valor = float(input('Qual valor que você deseja depositar? '))
                    if valor < 0:
                        print('Digite um valor valido!')
                    else:
                        cd.depositar(logar, valor, 1)
                    resp = str(input('Deseja depositar mais algum valor? [sim/nao]')).strip()
                    if resp == 'sim':
                        continue
                    else:
                        break
            elif func == 2:
                while True:
                    cd.saque(logar)
                    resp = str('Deseja depositar mais algum valor? [S/N]').upper()
                    if resp == 'sim':
                        break
                    else:
                        continue
            break
except Exception as e:
    print(f'Erro 1 Ocorreu um erro inesperado {e}. Por favor, tente novamente mais tarde! ')