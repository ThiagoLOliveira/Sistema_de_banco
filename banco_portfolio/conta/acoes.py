from principal import chave, entrada
from cliente import gera_cadastro
from comandos import depositar

import shutil

try:
    resp = str(input('Você ja tem cadastro? [S/N]')).strip().upper()
    if resp in 'sSSimSIM':
        logar = chave()
        entrar = entrada(logar)
    else:
        novo_cliente = gera_cadastro()
except Exception as e:
    print(f'Dados com erro: {e}')
finally:
    print('Obrigado por usar o Banco Python')


boas_vindas = "\033[1;47m\033[1mOque você deseja fazer? \033[0m\033[0m"
largura_terminal, _ = shutil.get_terminal_size()

boas_vindas = boas_vindas.center(largura_terminal)

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
                    valor = float(input('Qual valor que vocÊ deseja depositar? '))
                    if valor < 0:
                        print('Digite um valor valido!')
                    else:
                        depositar(logar, valor)
                    resp = str('Deseja depositar mais algum valor? [S/N]').upper()
                    if resp not in 'SsSimSIM':
                        break
                    else:
                        continue
            break
except Exception as e:
    print(f'Erro 1 Ocorreu um erro inesperado {e}. Por favor, tente novamente mais tarde! ')