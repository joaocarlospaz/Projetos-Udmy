# Crie uma lista com os números de 1 a 5.
# Imprima o índice e o número ao quadrado.
# Exemplo de saída:

# lista = [1, 2, 3, 4, 5]

# indices = range(len(lista))

# for indice in indices:
#     quadrado = lista[indice] ** 2
#     print(f'\n{indice} -> {quadrado}\n')

# 📝 Exercício 3 – Lista de preços

# Crie uma lista com 5 preços (números decimais).
# Imprima o índice e o preço formatado com duas casas decimais.

lista = [2, 5.333, 105.4999]

indices = range(len(lista))

for indice in indices:
    preco = lista[indice]
    print(f'{indice} - R$ {preco:.2f}')
    
