"""
🟡 Nível intermediário
1 Contar letras
Peça uma string e conte quantas vezes cada letra aparece.
2 Lista invertida
Dada uma lista, retorne ela invertida sem usar reverse().
3 Números únicos
Dada uma lista, retorne outra lista sem números repetidos.
4 Palíndromo
Verifique se uma palavra é igual de trás pra frente.
"""
# 1
texto = input("Digite uma palavra: ")

for letras in texto:
    print(letras, texto.count(letras))
print()

# 2
lista = [1, 2, 3, 4, 5]
print(lista[::-1])
print()

# 3
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
numeros = set(lista)
print(f"{numeros}")
print()

# chat
# numeros = []
# for n in lista:
#     if n not in numeros:
#         numeros.append(n)

# print(numeros)

# 4
texto = input("Digite uma palavra: ")

invertida = texto[::-1]

if texto == invertida:
    print(f"Sua palavra é Palíndromo: {texto}")
else:
    print("Não são iguais.")