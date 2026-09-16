from rich import inspect


"""
Classes -> São apenas os moldes
quem leva as informações, são as instancias.
classes levam com  si:
- atributos
- metodos
e sua instância
"""

class Pessoa:
    # __init__ é o primeiro metodo chamado, para incializar a classe
    def __init__(self, nome, sobrenome): # self ja é gerado automaticamente pela classe
        self.nome = nome                 # self -> seria a instacia
        self.sobrenome = sobrenome       # nome e sobrenome, os atributos da classe



# p1 = Pessoa()
# p1.nome = "João" # Atributo
# p1.sobrenome = "Carlos" # Atributo
p1 = Pessoa("Maria", "Clara")

print(p1.nome, p1.sobrenome)
print(p1)
inspect(p1)