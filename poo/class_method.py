from rich import print

# Class Method // Metodos de classes
# @classmethod -> usar a propria classe no lugar do self

class Pessoa():
    ano = 2023 # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def aniversario(cls, nome): # cls -> classe
        return cls(nome, 18)  # Usa-se diretamente a classe

p1 = Pessoa("João", 80)
p2 = Pessoa.aniversario("José")
p3 = Pessoa.aniversario("Bilu")



print(f"{p1.nome}, {p1.idade} :old_man:")
print(f"{p2.nome}, {p2.idade} :child:")
print(f"{p3.nome}, {p3.idade} :alien:")

