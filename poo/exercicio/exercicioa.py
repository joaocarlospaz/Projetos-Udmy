import json
from exerciciob import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

p1 = Pessoa(dados["nome"], dados["idade"])
print(dados)
print(p1.nome)
print(p1.idade)
