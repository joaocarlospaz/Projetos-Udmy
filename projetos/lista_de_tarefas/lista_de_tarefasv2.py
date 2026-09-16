import os

# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

lista = []
removidos = []

def escolher():
    escolha = input(
        "\nMenu: \n" \
        "Listar, refazer, desfazer e sair;\n" \
        "Adicione: " 
    )
    return escolha

def listar(tarefas):
    print()
    if not tarefas:
        print("Não tem o que ser listado")
    else:
        for l in tarefas:
            print(l) 

def adicionar(tarefas):
    tarefas.append(escolha)

def desfazer(tarefas):
    print()
    if not tarefas:
        print("Não a oque desfazer")
    else:
        remocao = tarefas.pop()
        removidos.append(remocao)
        listar(lista)

def refazer(tarefas):
    print()
    if not removidos:
        print("Não tem o que refazer")
    else:
        tarefas.append(removidos[-1])
        removidos.pop()
        listar(lista)
        
while True:

    escolha = escolher()

    if escolha.lower() == "listar":
        listar(lista)
    elif escolha.lower() == "refazer":
        refazer(lista)
    elif escolha.lower() == "desfazer":
        desfazer(lista)
    elif escolha.lower() == "sair":
        break
    elif escolha.lower() == "clear":
        os.system("cls")
    else:
        adicionar(lista)

    



    
