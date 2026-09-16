# copy, sorted, produtos.sort
# copy para copia
# sorted parar alinhar os produtos em ordem

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# multiplicar por 0.100

# Gere novos_produtos por deep copy (cópia profunda)
# com copy

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)\
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# novos_produtos = copy.deepcopy(produtos) # usar deepcopy, posso alterar valores
# sem que altere na original
# novos_produtos = copy.copy(produtos) # Já no copy, que é uma rasa
# Se eu alterar na nova, altera na original.

# DESSA FORMA NAO TAVA USANDO DEEP COPY
# novos_produtos = []
# for lista in produtos:
#     novo_valor = round(lista["preco"] * 0.100 + lista["preco"], 2)
#     lista["preco"] = novo_valor
#     novos_produtos.append(lista)
novos_produtos = copy.deepcopy(produtos)
print("Produtos: ")
print(*produtos, sep= "\n")

for produto in novos_produtos: # Aqui poderia se usar uma list comprehesion
    # produto for produto in noso_produtos # já me daria esse resultado
    produto["preco"] = round(produto["preco"] * 1.10, 2) # round, arredonda o valor

print("\nPreços atualizados: ")
print(*novos_produtos, sep= "\n")

# produtos_ordenados_por_nome = copy.deepcopy(novos_produtos) # inves de criar uma variavel

produtos_ordenados_por_nome = sorted( # Prefira legibilidade acima de escrever menos linhas.
    copy.deepcopy(novos_produtos), # colocar já dentro da variavel não afeta a expressão.
    key = lambda item: item["nome"],
    reverse = True
    )

print("\nProdutos ordenados por nome(decrescente): ")
print(*produtos_ordenados_por_nome, sep= "\n")
 
produtos_ordenados_por_precos = sorted(
    copy.deepcopy(novos_produtos), # fazer a deep copy dentro seria mais legivel, e melhor de se codar
    key = lambda item: item["preco"]
    )


print("\nProdutos ordenados por preço(crescente): ")
print(*produtos_ordenados_por_precos, sep= "\n")

