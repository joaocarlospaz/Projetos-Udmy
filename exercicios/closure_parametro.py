def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def executar(funcao, x):
    def argumento(y):
        return funcao(x, y)
    return argumento


somar = executar(soma, 5)
multiplicar = executar(multiplica, 2)

print(f"soma = {somar(5)}")
print(f"multiplicação = {multiplicar(5)}")