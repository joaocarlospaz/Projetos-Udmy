# Exercicios com funções

"""
1.
Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variavél e mostre o valor
da variavel
2.
Crie uma função que fala se um número é par ou ímpar
Retorne se o número é par ou impar.
"""

def multiplicar(*args): # Empacotando meus argumentos
    total = 1
    for n in args:
        total *= n
    def par(x):
        condicao = x % 2 ==0
        variavel = "Par" if condicao else "Impar"
        print(variavel)
    par(total)
    print(total)
    return total

#Regra de ouro (guarda isso!)
#print() = mostrar na tela
# return = devolver valor pra variável

numeros = 3, 3
multiplicacao = multiplicar(*numeros) # Faz o desempacotamento e transforma em número;

#Resumão pra guardar

#*args na função → 
# empacota vários valores em uma tupla
#* na chamada → 
# desempacota uma tupla/lista em vários valores







# multiplicacao2 = multiplicar(1, 2, 3, 4, 5)
# print(multiplicacao2)
# def par(x):
#     condicao = x % 2 ==0
#     variavel = "Par" if condicao else "Impar"
#     print(variavel) 
   
# par(5)