# Criar um programa onde o usuário pode:

# Adicionar tarefas
# Listar tarefas
# Remover tarefas
# Sair do programa

tarefas = []

while True:
    try:
        acao = int(input( 
        "1. Adicionar Tarefas;\n"
        "2. Listar Tarefas;\n"
        "3. Remover Tarefas;\n"
        "4. Sair do Programa.\n"
        "Digite sua função: \n"))
        
        if acao == 1:
            tarefas_adicionadas = input("Digite a tarefa que deseja adicionar: ")
            tarefas.append(tarefas_adicionadas)
        elif acao == 2:
            for numero, tarefa in enumerate(tarefas, start=1): # Para já começar do 1
                print(f"{numero}. {tarefa};")
        elif acao == 3:
            tarefas_removidas = int(input("Digite a tarefa que deseja remover: "))
            tarefas.pop(tarefas_removidas, start=1)
        elif acao == 4:
            print("Você saiu!")
            break
        
    except ValueError:
        print("Digite apenas números.") 
      