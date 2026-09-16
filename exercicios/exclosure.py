# Função 1
def enter_multiplier(multiplier): # Escopo Global {multiplier}
    def multiplication(number): # Escopo Local {number}
        return number * multiplier # Operação
    print(f"\nFunction 1\n" # Número do exercicio
          f"Multiplicado por {multiplier}:") # Mostra o multiplicador
    return multiplication # Retorna a operação

operation = enter_multiplier(5) # Define o multiplicador
print(
    f"{operation(2)}" # Defino o número
)

print("\n====================================\n")
# Função 2
def enter_gretting(grett): # Saudação
    def enter_name(name): # Def para definir o nome
        return f"{grett}, {name}!" # Retornar a saudação e nome.
    return enter_name
# Defino a saudação, então segue pro return enter_name, falta definir o nome
bom_dia = enter_gretting("Bom dia")
boa_tarde = enter_gretting("Boa tarde")
boa_noite = enter_gretting("Boa Noite")
# Defino o nome
print(
    f"Funtion 2\n"
    f"{bom_dia("João")}\n"
    f"{boa_tarde("João")}\n"
    f"{boa_noite("João")}"
    )
print("\n====================================\n")
# Função 3
# total = 0 # Global
def contador():
    total = [0]
    def number():
        total[0] += 1
        return total[0]
    return number

quantidade = contador()
print(
    f"Function 3\n"
    f"{quantidade()}"
    )
print(quantidade())        
print(quantidade())        
print(quantidade())
print("\n====================================\n")
# Função 4
def acumulador(): # Criei uma função que retorna o valor da closure
    acumulando = 0 # Variavel externa IMUTAVEL, pois é int
    def acumulo(*args): # Criei uma função com *args, pois podem ser varios argumentos
        nonlocal acumulando # Reatribuindo valor a variavel com nonlocal
        for i in args: # For para, caso for uma lista, passar de um em um e somar
            acumulando += i # somar
        return acumulando # Retorna o total da minha função
    return acumulo # retorna o valor de da função acumulo

soma = (acumulador())
print("Function 4")
print((soma(5)))
numbers = 10, 5, 5
print(soma(*numbers))
print(soma(10, 5, 5))
print("\n====================================\n")     
# Função 5
def desconto(number):
    def aplicando(valor):
        return valor - number
    return aplicando

desconto_10 = desconto(10)
print(
    f"Function 5\n"
    f"O Desconto do seu produto foi aplicado, {desconto_10(100)}!"
)
print("\n====================================\n") 
# Função 6
def validador(valor):
    def validar(valida):
        condicao = valor >= valida
        return "Valido" if condicao else "Invalido"
    return validar

parametro = validador(18) # Guarda na memoria, na variavel no caso
print(f"Function 6\nO seu valor é {parametro(20)}!")
print(f"O seu valor é {parametro(15)}!")

        


