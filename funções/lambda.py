# Função lambda, é uma função como qualquer outra, mas em uma linha
# lambda parâmetros: expressão
# Vantangens -> melhor legibilidade, uso para coisas pequenas
# Desvantagens -> usado apenas para pequenas ações

numero = int(input("Digite um número para dobrar: "))

somar = lambda x, y: x + y
dobrar = lambda n: n * 2

print(f"Soma de {numero}: {somar(10, 5)}")
print(f"Dobro de {numero}: {dobrar(numero)}")