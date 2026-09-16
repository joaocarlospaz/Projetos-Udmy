# Cria uma classe que receba:
# nome e valor + um método que retorne uma etiqueta
from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, valor = 0):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        etiqueta = Panel(f"    {self.nome} \n"
                         f"----------------\n"
                         f"----R${self.valor:,.2f}----", title= "[bold black]Produto[/]", width=20)
        return etiqueta

bolacha = Produto("Bolacha", 4)
print(bolacha.etiqueta())