# Exercício 4 - Dicionários

# Você recebeu:

alunos = {
    "João": 8,
    "Maria": 10,
    "Pedro": 6,
    "Lucas": 9,
    "José": 5
}

# Faça um programa que:

# mostre todos os alunos e notas;

for aluno, nota in alunos.items():
    print(f"Aluno(a): {aluno}, tirou {nota}.") 

# calcule a média das notas;

resultado = 0

for nota in alunos.values():
    resultado += nota
    media = resultado / len(alunos)

print(f"\nMédia de notas da turma: {media}.\n")

# mostre quem tirou a maior nota;
maior_nota = None 
maior_aluno = ""
menor_nota = None
menor_aluno = ""

for aluno, nota in alunos.items():
    if maior_nota is None or maior_nota < nota:
        maior_nota = nota
        maior_aluno = aluno
  
    if menor_nota is None or menor_nota > nota:
        menor_nota = nota
        menor_aluno = aluno

print(f"A maior nota da sala foi de {maior_aluno}: {maior_nota}")
print(f"Já a menor nota, foi {menor_aluno}: {menor_nota}\n")

# mostre quem tirou nota menor que 7. 

for aluno, nota in  alunos.items():
    if nota < 7:
        print(f"{aluno}, abaixo da media(7), nota {nota}.")

