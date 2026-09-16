"""
Crie uma função que dê o dobro, triplo e o quadruplo.
"""
def multiply(number2):
    def multipycation(number):
        return number * number2
    return multipycation

dobrar = multiply(2)
triplicar = multiply(3)
quadruplicar = multiply(4)

print(dobrar(2))