"""
2. Exercícios simples (20 min)
Exercício 1
Crie um dicionário com:
nome
idade
profissão
E imprima tudo.
"""

# perfil = {
#     "nome": "João",
#     "idade": "20",
#     "profissão": "Aux. Lógistica II"
# }

# print(perfil)

"""
Exercício 2
Peça nome e idade ao usuário e armazene em um dicionário.
"""

# nome = input("Me dê seu nome, para cadastro: ")
# idade = input("Agora me informe sua idade: ")

# perfil = {}
# # dicionario[chave] = valor
# perfil["nome"] = nome
# perfil["idade"] = idade
# print(perfil)

# 4. Exercício final (15 min)
# Crie um pequeno cadastro:
# pessoas = [
#     {"nome": "João", "idade": 20},
#     {"nome": "Maria", "idade": 18},
# ]
# Depois percorra a lista e mostre os dados de cada pessoa.


pessoas = [
    {"nome": "João", "idade": 20},
    {"nome": "Marlon", "idade": 6}
    ]

for pessoa in pessoas:
    for chave, valor in pessoa.items():
        print(chave, ":", valor)
    print()

print(f"{pessoas[0]["nome"]} tem {pessoas[1]["idade"]} anos.")
# Caso eu queira pegar valores especificos, apenas colocar dentro de conchetes.