from rich import print

# Criar uma classe que recebe:
# nome, setor e cargo de um funcionario;
# com um método de apresentação

class Funcionario:
    empresa = "Avelloz" # atributos de classe
    def __init__(self, nome, setor, cargo): 
        self.nome = nome # atributos de instância
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return print(f"Meu nome é [blue]{self.nome}[/] :grin: "
                f"sou do setor de [green]{self.setor}[/] "
                f"e ocupo o cargo de [red]{self.cargo}[/] "
                f"na {Funcionario.empresa} :bike: ;")

funcionario = Funcionario("João", "Lógistica", "Auxiliar de Lógistica II")
funcionario.apresentacao()