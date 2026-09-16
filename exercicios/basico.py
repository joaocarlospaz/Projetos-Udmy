# Nível básico

# 1 Par ou ímpar
# Peça um número ao usuário e diga se é par ou ímpar.

# 2 Maior número
# Peça 3 números e mostre qual é o maior.

# 3 Contagem
# Mostre os números de 1 até 10 usando for.

# 4 Soma de lista
# Dada uma lista [1, 2, 3, 4, 5], calcule a soma sem usar sum().

# ================================================= #
# 1
print("PAR ou ÍMPAR")
numero = int(input("Digite um número: "))

par = numero % 2 == 0
checagem = "Par" if par else "Ímpar"

print(checagem)
print()

# 2
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

maior = max(n1, n2, n3)
print(maior)
print()

# 3
for n in range(1, 11):
    print(n)
print()

# 4
lista  = [1, 2, 3, 4, 5]
soma = 0
for n in lista:
    soma += n
print(soma)
