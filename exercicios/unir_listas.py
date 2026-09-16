
# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']     
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

import itertools

city = ["Salvador", "Ubatuba", "Belo Horizonte"]
state = ["BA", "SP", "MG", "RJ"]

# def zipper(list1, list2):
#     for c, s in zip(list1, list2): # zip une listas e entrega os valores separados.
#         print(f"{c} - {s}")
        
# def zipper(list1, list2):
#     intervalo = min(len(list1), len(list2))
#     return [(list1[i], list2[i]) for i in range(intervalo)] #list comprehesion
#     # for i in range(intervalo):
#     #     print(list1[i], list2[i]) 

print(list(itertools.zip_longest(city, state)))
for i in itertools.zip_longest(city, state, fillvalue= "sem cidade"):
    print(i)
