# Exercício 1 - Closure (Fácil)
# Crie uma função multiplicador(fator) que retorne outra função.

def multiplicador(fator):
    def multiplicar(numero):
        return fator * numero
    return multiplicar

dobro = multiplicador(2)
triplo = multiplicador(3)

print(dobro(5))
print(triplo(5))
