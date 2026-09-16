"""
Introdução a try/except
try -> tentando executar um código
except -> ocorreu algum erro ao tentar executar
if e else são para lógica, try/except são para erros (exceptions).

if numero_str.isdigit(): # checando uma condição.
    numero_float = float(numero_str)
    print(f'O dobro do número {numero_str}, é {numero_float * 2}.')

else:
    print('Você não digitou um número.')
"""

numero_str = input('Vou dobrar o número que você digitar: ')


try:
    numero_float = float(numero_str)
    print(f'O dobro do número {numero_str}, é {numero_float * 2}.')
except:
    print('Isso não é um número')