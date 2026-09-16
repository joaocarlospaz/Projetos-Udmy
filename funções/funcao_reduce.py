from functools import reduce

# reduce serve para reduzir o iteravel a um argumento
# Geralmente usado para entregar o total de um iteravel
# reduce(acumulador, produto, valor inicial)
# reduce recebe:
# 1. função
# 2. iteravel
# 3. valor inicial
# reduce faz a iteração de cada iteravel

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def acumular_valores(acumulador, produto):
    print(acumulador) 
    print(produto)
    return acumulador + produto["preco"]

# reducao = reduce(
#             lambda acumulador, p: acumulador + p['preco'], # função
#         produtos, # iteravel
#         0 # valor inicial
# )


reducao = reduce(
    acumular_valores, # funcao
    produtos, # iteraval
    0 # valor inicial
)

print() 
print(f"Valor total = {reducao:.2f}")