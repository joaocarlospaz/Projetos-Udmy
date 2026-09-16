# Remover espaços
# Peça uma frase e exiba a mesma frase sem espaços (sem usar .replace()).

frase = input("Digite uma frase: ")
i = 0
sem_espacos = ""

while i < len(frase):
    if frase[i] != " ":
        sem_espacos += frase[i] 
    i += 1

print(f"Frase sem espaços:\n {sem_espacos}")