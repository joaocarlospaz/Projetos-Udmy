# Calculadora 

def rodar():
    while True:
        operador = input("Operador: ")   
        try:
            numero1 = float(input("Número: \n"))
            numero2 = float(input("Número: \n")) 
            if operador in "+-/*":
                def calcular(x, y):
                    if operador == "+":
                        print(x + y)
                    if operador == "-":
                        print(x - y)
                    if operador == "*":
                        print(x * y)
                    if operador == "/":
                        print(x / y)
                return calcular(numero1, numero2)
            else:
                print("Digite um operador valido")
        except ValueError:
            print("Digite um número.")


rodar()