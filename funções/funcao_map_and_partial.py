from functools import partial
from types import GeneratorType

# Função map -> map(funcao, iteravel)
# a função map: recebe uma função e um iteravel
# a função, tanto faz for def ou lambda
# Ex.: 
# com def:

# def iteravel(iteravel): 
#     return iteravel * 2

# Ex.: 
# com lambda

numeros = [1, 2, 3, 4]
print("Anotações sobre 'map': ")
print(
    "Dobro de cada número: ",
    list(map( 
        lambda x: x * 2, numeros
))
)
print()

# funcao partial do modulo functools
# partial é usado para guardar o valor de uma função (closure)
# partial -> recebe uma função e o argumento da função, podem ser um ou vários
# Ex.:

print("Anotações sobre 'partial': ")
def multiplicar(x, y):
    return x * y

dobro = partial(multiplicar, y=2) # guardou o valor sem precisar de uma closure
triplicar = partial(multiplicar, y=3)

print("Operação: ",multiplicar(2, 5)) 
print("Dobro: ", dobro(2))
print("Triplo: ", triplicar(2))
print()

# modulo para saber se é um generator -> GerenatorType
# modulo types, tem um objeto chamado GeneratorType, pra saber se é um generator
# Ex.: 
print("Anotações sobre GeneratorType: ")
print(isinstance(numeros, GeneratorType))