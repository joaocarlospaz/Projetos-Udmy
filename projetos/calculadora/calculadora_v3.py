from os import system

def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

def potencializar(x, y):
    return x ** y

def ler_numeros():
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    return numero1, numero2

def operacao(a, x, y):
    return a(x, y)
     
def exec_opcao():
    opcao = int(input(
        "Deseja continuar?: \n"
        "1. Sim\n"
        "2. Não\n"
        "Opcão: "))
    return opcao
     
while True:
    try:
        escolha = int(input( 
                "Menu - Calculadora: \n" \
                "Digite o número correspondente a ação: \n" \
                "1. Somar \n" \
                "2. Multiplicar \n" \
                "3. Subtrair \n" \
                "4. Dividir\n" \
                "5. Potência\n" \
                "6. Sair\n" \
                "Escolha: "
        ))
    except ValueError:
        print("\nDeve ser um número.\n")
        continue

    if escolha == 1:
        system("cls")
        print("1. Somar: ")
        try:
            n1, n2 = ler_numeros()
            soma = operacao(somar, n1, n2)
            print(f"O resultado é {soma}")
            print(soma)
            opcao = exec_opcao()
            if opcao == 1:
                system("cls")
                continue
            else:
                break
        except ValueError:
                print("\nDeve ser um número.\n")
                continue
        
    elif escolha == 2:
        system("cls")
        print("2. Multiplicar: ")
        try:
            n1, n2 = ler_numeros()
            multiplica = operacao(multiplicar, n1, n2)
            print(f"resultado: {multiplica}")
            opcao = exec_opcao()
            if opcao == 1:
                system("cls")
                continue
            else:
                break
        except ValueError:
                print("\nDeve ser um número.\n")
                continue
        
    elif escolha == 3:
        system("cls")
        print("3. Subtrair: ")
        try:
            n1, n2 = ler_numeros()
            subtrai = operacao(subtrair, n1, n2)
            print(f"resultado: {subtrai}")
            opcao = exec_opcao()
            if opcao == 1:
                system("cls")
                continue
            else:
                break
        except ValueError:
                print("\nDeve ser um número.\n")
                continue  
              
    elif escolha == 4:
        system("cls")
        print("4. Dividir: ")
        try:
            n1, n2 = ler_numeros()
            divide = operacao(dividir, n1, n2)
            print(f"resultado: {divide}")
            opcao = exec_opcao()
            if opcao == 1:
                system("cls")
                continue
            else:
                break
        except (ValueError, ZeroDivisionError) as error:
                print(f"\n{error} - Deve ser um número > que 0.\n")
                continue
        
    elif escolha == 5:
        system("cls")
        print("5. Potência: ")
        try:
            n1, n2 = ler_numeros()
            potencia = operacao(potencializar, n1, n2)
            print(f"resultado: {potencia}")
            if opcao == 1:
                system("cls")
                continue
            else:
                break
        except ValueError:
                print("\nDeve ser um número.\n")
                continue
    elif escolha == 6:
         break
    else:
        print("\nDigite um número do menu.\n")
        continue

