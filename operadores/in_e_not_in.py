"""
Operadores Lógicos 
in e not in
Strings são iteráveis
 0 1 2 3 4 5 
 O t á v i o
 -6-5-4-3-2-1
"""
nome = 'Otávio'
print('Testando funções in e not in. \n')
print(nome[2])
print(nome[-4])
print(10 * '-')
print('á' in nome ) # Esta entre as letras do nome.
print('vio' in nome ) # Esta entre as letras do nome.
print(10 * '-')
print('á' not in nome ) # Não esta entre as letras do nome.
print('vio' not in nome) # Não esta entre as letras do nome.
print(10 * '-')
n2 = input('Digite seu nome: ')
encontrar = input('Digite oq deseja encontrar: ')

if encontrar in nome:
    print(f'"{encontrar}" esta no nome {n2}.')
else:
    print(f'"{encontrar} não esta no nome {n2}."')