# Criar uma lista de compras onde possa, apagar, inserir e listar itens;
# Não deixe o programa romper.
import os

lista = []

while True:
    opcao = input("Selecione uma opção: \n[i]nserir [a]pagar [l]istar [v]isualizar: ").lower()

    if opcao == "a":
        if len(lista) == 0:
            os.system("cls")
            print("Não a nada na lista.")
        else:
            try:
                apagar = int(input("Apagar índice: "))
                lista.pop(apagar)
            except (ValueError, IndexError):
                print("Índice inválido.")
    elif opcao == "i": 
        inserir = input("Inserir: ")
        os.system("cls")
        print(inserir)
        lista.append(inserir)
    elif opcao == "l":
        for a, b in enumerate(lista):
            print(a, b)
    elif opcao == "v":
        print(lista)
    else:
        os.system("cls")
        print("Por favor, escolha uma opção.")