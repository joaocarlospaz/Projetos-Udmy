# Declaração de Classe
class Gafanhoto():
    """
    Classe Gafanhoto
    recebe dois atributos para usar defina:
    nome, idade
    retorna nome é Gafanhoto e tem idade anos de idade.
    """
    def __init__(self, nome= "", idade=0): # Iniciador, obrigatorio em toda class
        # Atributos da classe
        self.nome = nome
        self.idade = idade

    # Metódos da Classes
    def aniversario(self):
        self.idade += 1        

    def __str__(self): # Dunder Method
        return f"\n{self.nome} is 'Gafanhoto(a)' and have {self.idade} years old."

    def __getstate__(self): # Method
        return f"Estado: nome = {self.nome} idade = {self.idade}"

g1 = Gafanhoto("João", 20) # Declaração de instância
g1.aniversario()
print(g1)

print(g1.__class__)
print(g1.__doc__)
print(g1.__dict__) # Attribute // Transforma em um dicionario
print(g1.__getstate__()) # Method // mesma coisa, mas posso personalizar