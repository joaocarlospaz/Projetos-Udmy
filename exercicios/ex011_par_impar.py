"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

number = input('Digite um número: ')

try:
    numero_int = int(number)
    par = numero_int % 2 == 0 
    impar = numero_int % 2 != 0 

    if par:
        print('O número que você digitou é par.')
    elif impar:
        print('O número que você digitou é impar.')

except:
    print('Você não digitou um número inteiro.')
