"""
zip(), junta duas listas e entrega os valores separados
for a, b in zip(lista1, lista2)

↓ vira

(lista1[0], lista2[0])
(lista1[1], lista2[1])
(lista1[2], lista2[2])
"""

nomes = ["João", "Maria", "Joana"]
idades = [20, 19, 18]

for nome, idade in zip(nomes, idades):
    print(f"Nome: {nome} - idade {idade} anos")

