# Contador de caracteres específicos
# Conte quantas vezes a letra “a” aparece em uma frase digitada.

frase = input("Digite uma frase: ").lower()
# letra = frase.count("a") # Já faz isso tudo
# print(f"A letra 'a', apareceu {letra} vezes.")
i = len(frase)
a = 0
contador = 0

while contador < i:
    if frase[contador] == "a":
        a += 1
    contador += 1
print(f"A vogal 'a', apareceu {a} vezes.")
    
