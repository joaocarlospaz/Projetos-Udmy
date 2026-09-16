# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
pessoa = {
    "nome": "Luiz Otávio",
    "sobrenome": "Miranda",
    "idade": 18,
    "altura": 1.8,
    # "enderecos":[
    #     {"rua": "tal tal", "número": 123},
    #     {"rua": "tal tal", "outro" "número": 123},
    # ],
}
# pessoa = dict(nome= "João", sobrenome= "Carlos") # Outra forma de criar dicionario
# pessoa = {} # Para criar um dicionario
print(pessoa, type(pessoa))
print(pessoa["nome"]) # para acessar usa-se conchetes, como se fosse um indice da lista
print(*pessoa.keys())

print()