from principal import chave, entrada
from cliente import gera_cadastro
from random import randint
import shutil

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


boas_vindas = "\033[1;47m\033[1mOque você deseja fazer? \033[0m\033[0m"
largura_terminal, _ = shutil.get_terminal_size()

boas_vindas = boas_vindas.center(largura_terminal)

print('-' * largura_terminal)
print(boas_vindas)
print('-' * largura_terminal)
print('[1] DEPOSITO BANCARIO')
print('[2] SAQUE DA CONTA')
print('[3] EXTRATO BANCARIO')