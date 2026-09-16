from rich import print
from rich.panel import Panel

# Criação de paineis
# podendo alterar, titulos, largura, estilo de cores e etc...
painel = Panel("[white]Painel para testes:+1:...[/]", title="[bold black]Painel[/]", style="red", width= 50)
print(painel)