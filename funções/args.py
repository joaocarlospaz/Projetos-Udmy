# args = Argumentos não nomeados
# * - *args (empacotamento e desempacotamento)
# Transforma numa tupla

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args): # args empacota
    total = 0
    for numero in args:
        total += numero
    return total # return sempre no def

numeros = 1, 2, 3, 4, 5, 6
sum1 = soma(*numeros) # desempacota sem ser uma tupla
print(sum1)
print(sum(numeros)) # desempacota, mas aqui é uma tupla
