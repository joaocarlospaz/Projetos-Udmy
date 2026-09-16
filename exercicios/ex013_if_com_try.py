"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')

try:
    letras = len(nome)
    if letras <= 4:
        print('Seu nome é muito curto.')
    elif letras > 4 and letras < 7:
        print('Seu nome é normal.')
    elif letras > 6:
        print('Seu nome é muito grande.')
except:
    ('Isso não é um nome.')