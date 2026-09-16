# Declaração de Classe
class Gafanhoto():
    def __init__(self): # Iniciador, obrigatorio em toda class
        # Atributos da classe
        self.nome = ""
        self.idade = 0

    # Metódos da Classes
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f"\n{self.nome} is 'Gafanhoto(a)' and have {self.idade} years old."

g1 = Gafanhoto() # Declaração de instância
g1.nome = "João"
g1.idade = 20
g1.aniversario()

print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Glória"
g2.idade = 20
g2.aniversario()

print(g2.mensagem())