# Programação funcional
# filter, filtrar valores
# recebe uma função e um iteravel
# Ex.:


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Tipos de filtragem:

filtrar = [ 
    p for p in produtos
    if p["preco"] > 10
] 

print(
    *list(
    p for p in produtos
    if p["preco"] > 10)
)
print()

print(*filtrar)
print()

print(
    *list(
        filter(
        lambda p: p["preco"] > 10, produtos  
    )
    )
)
