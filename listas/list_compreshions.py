# # print(list(range(10)))
# lista = [numero for numero in range(10)]
# print(lista)
# # logica antes do for
# lista = [numero * numero for numero in range(10)]
# print(lista)
"""
Mapeamento quer dizer que ta pegando dados e deixando do mesmo tamanho
Mapeamento de dados em list comprehesion
produtos = [ 
]
O que vem na esquerda do for é mapeamento, na esquerda é filtro
"""
lista = [n for n in range(10) if n < 5] 
# filtragem dos numeros

dobro = [x**2 for x in range(1, 11) if x <= 5] # Exemplo de mapeamento e filtragem.

print(*dobro, sep= "\n")

chamada = ["João"]
nomes = [(x, y) for x in [1, 2, 3] for y in [4, 1, 2] if x != y]

print(*nomes)