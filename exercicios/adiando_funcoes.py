# Adiando funções

def soma(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

def executar(funcao, *args):
    def argumento(y):
        return funcao(y, *args)
    return argumento # Se eu deixar sem parenteses so vai guardar na memoria

soma_por_cinco = executar(soma, 5)
print(soma_por_cinco(15))

multiplica_por_dez = executar(multiplicar, 10)
print(multiplica_por_dez(2))

dividir_por_dois = executar(dividir, 2)
print(dividir_por_dois(10))
    


