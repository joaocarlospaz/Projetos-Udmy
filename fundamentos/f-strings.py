"""
Formatação básica de strings
s - strings 
d - int 
f - float 
.<número de dígitos>f
x ou X hexadecimal
(Caractere)(><^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer dps do zero.
Sinal - + ou -
Ex: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #PAD
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:+,.1f}')
