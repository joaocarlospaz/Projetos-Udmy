# Considerando duas listas de inteiros ou floats (lista A e lista B)
# Some os valores nas listas retornando uma nova lista com os valores somados:
# Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
# menor.

# Exemplo:

# lista_a     = [1, 2, 3, 4, 5, 6, 7]
# lista_b     = [1, 2, 3, 4]

# =================== resultado

# lista_soma  = [2, 4, 6, 8]

# 2
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista = list(zip(lista_a, lista_b, fillvalue= 0)) # zip() aó une a lista até o tam da lista menor
# lista = list(itertools.zip_longest(lista_a, lista_b, fillvalue= 0)) 
somadas = [(x + y) for x, y in lista]
print(somadas)

#1

# intervalo = min(len(lista_a), len(lista_b))

# print([(lista_a[i] + lista_b[i]) for i in range(intervalo)])

