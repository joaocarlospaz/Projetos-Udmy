# Exiba os indices da lista.

lista = ["João", "Carlos", "Paz"] # lista

lista.append("Junior")
lista.insert(0, "Nino")
for i in range(len(lista)): # "i" representando indices.
    print(f"Nome: {lista[i]} \nindice: {i}") # "i" no range, como cada indice da lista.
# easy