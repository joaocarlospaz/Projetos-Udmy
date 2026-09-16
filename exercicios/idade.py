def idade(x):

    try:
        if x <= 0:
            print("Idade inválida, Digite um número.")
        else:
            print(f"Idade {x} válida!")
        
    except TypeError:
        print("Por favor, digite um número inteiro.")
    

idade(x = 5)