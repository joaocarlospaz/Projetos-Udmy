from rich import print
from rich.table import Table

# Criação de tabelas
# Podendo adicionar colunas/linhas e personaliza-las
tabela = Table(title="Tabela de preços")
tabela.add_column("Nome", justify= "center")
tabela.add_column("Preço", justify= "center", style="red")
tabela.add_column("Estoque", justify= "center", style="red")

tabela.add_row("[blue]Lápis[/]", "R$1.00", "0")
tabela.add_row("[blue]Borracha[/]", "[green]R$1.50[/]", "[green]5[/]")

print(tabela)