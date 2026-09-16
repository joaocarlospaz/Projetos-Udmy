
salas = [
#      0        1
    ["João", "Maria"], # 0 
#      0
    ["Helena"], # 1 
#      0        1           2               3
    ["Jorge", "Mateus", "Luciano"] #(0, 10, 20, 30, 40)] # 2
]

# print(salas[0])
# print(salas[0][1])
# print(salas[2][3][2])

for sala in salas:
    print(f"A sala é {sala} e os alunos: ")
    for aluno in sala:
        print(aluno) 

