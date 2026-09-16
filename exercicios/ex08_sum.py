# 1. Soma dos elementos
# Peça ao usuário uma lista de números (ex: 1, 2, 3, 4) e mostre a soma total dos elementos usando um for.

entrada = input("Digite números separados por vírgula: ")
numeros = [int(n.strip()) for n in entrada.split(',')]
print(f"A soma é: {sum(numeros)}")
