# Aula sobre groupby
# Para acessar groupby precisa importar itertools
# Agrupa valores de acordo com a key
# os valores precisam estar em ordem pra ser agrupados
# #Ex.:
# Certo -> a, a, a
# Errado -> a, a, b, a

from itertools import groupby

students = [
    {"Aluno": "João", "Nota": "A"},
    {"Aluno": "Maria", "Nota": "D"},
    {"Aluno": "Bruno", "Nota": "A"},
    {"Aluno": "Sato", "Nota": "B"}
]

# student = ["A", "A", "A", "B", "C", "D"] -> Grupo de teste

student = sorted(students, key=lambda s: s["Nota"]) # pra ordenar as letras, pra agrupar certinho
# key=lambda s: s["Nota"]) -> serve para pegar o valor da chave, "Nota";
# sorted(students, key=lambda s: s["Nota"]) - > como tem dicionarios, apenas sorted não vai funcionar;
# temos que definir o valor que ele deve se basear para ordenar;      

groups = groupby(student, key=lambda g: g["Nota"]) # Agrupar de acordo com a letra

for key, group in groups: # groupby retorna uma key e o grupo.
    print(key) # key
    for g in group: # cada grupo, de acordo com a key
        print(g)
