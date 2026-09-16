# Contar vogais
# Solicite uma palavra e conte quantas vogais ela possui usando while.

palavra = input("Digite uma palavra: ").lower()
vogais = "aeiou"
i = 0
contador = 0

while i < len(palavra):
    if palavra[i] in vogais:
        contador += 1
    i += 1

print(f"A sua tem {contador} vogais.")