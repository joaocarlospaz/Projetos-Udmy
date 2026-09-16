# Exercício 5 - Dicionários (Médio)
# Crie um pequeno sistema de estoque.
# Menu:
# 1 - Adicionar produto
# 2 - Alterar quantidade
# 3 - Remover produto
# 4 - Mostrar estoque
# 5 - Sair
# O estoque deve ser um dicionário.
# Exemplo:
# {
#     "Arroz": 10,
#     "Feijão": 5,
#     "Macarrão": 8
# }

estoque = {}
# chave = input(":")
# name = input("Digite um nome: ")
# estoque[chave] = name
while True:
    try:
        comando = int(input("Menu: \n"
        "1 - Adicionar produto\n"
        "2 - Alterar quantidade\n"
        "3 - Remover produto\n"
        "4 - Mostrar estoque\n"
        "5 - Sair\n"
        "Escolha de 1 a 5: "))
    except ValueError:
        print("Digite um número.\n")
        continue

    if comando == 1: # 1 - Adicionar produto
        print("\nAdicionar: ")
        produto = input("Produto: ")
        try:
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Digite um número.\n")
            continue    
        estoque[produto] = quantidade
        print("\n")

    elif comando == 2: # 2 - Alterar quantidade
        if len(estoque) == 0:
            print("\nEstoque vazio.\n")
        else:    
            print("Alterar quantidade: ")
            for produto, quantia in estoque.items():
                print(f"{produto} -> {quantia};")
            escolhido = input("Digite o produto que deseja alterar a quantidade: ")
            try:
                novo_valor = int(input("Qual seria a nova quantidade? "))
            except ValueError:
                print("Digite um número.\n")
                continue
            if escolhido not in estoque.keys():
                print("O Produto, escolhido não existe.")
            else:    
                estoque[escolhido] = novo_valor
                print("Valor atualizado, selecione a opção 4 para visualizar!")

    elif comando == 3: # - Remover produto
        if len(estoque) == 0:
            print("\nEstoque vazio.\n")
        else:
            print("Remover produto: ")
            for produto, quantia in estoque.items():
                print(f"{produto} -> {quantia};")
            produto_remocao = input("Digite o produto a ser removido: ")
            if produto_remocao not in estoque.keys():
                print("Produto não existe\n")
            else:    
                estoque.pop(produto_remocao)
                print("Produto removido, selecione a opção 4 psara visualizar!\n")
    
    elif comando == 4: # Mostrar estoque
        if len(estoque) > 0:
            for produto, quantia in estoque.items():
                print(f"{produto} -> {quantia};")
                # print(*produtos, sep = " -> ")
        else:
            print("\nEstoque vazio.\n")

    elif comando == 5: # Sair
        print("Até mais.")
        break
    