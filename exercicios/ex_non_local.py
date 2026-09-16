# Exercício 2 - nonlocal (Médio)
# Crie uma função contador() que retorne outra função.
# Toda vez que a função retornada for chamada, ela deve aumentar o contador em 1.

def contador(x = 0):
    a = x
    def acao():
        nonlocal a
        a += 1
        return a
    return acao

contar = contador() # Usa-se variavel pra armazenar o valor da função
# print(contador()()) # mas sempre vai retornar 1, por que não ta guardando o valor numa variavel
# print(contador()) # valor guardado na memoria
# contador() # nada
print(contar())
print(contar())
print(contar())
print(contar())

