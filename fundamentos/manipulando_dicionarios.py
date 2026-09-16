# Manupulando chaves e valores em dicionarios
pessoa = {}

chave = "nome" # Criar uma chave
pessoa[chave] = "Luiz Otávio" # Acessar uma chave

print(pessoa[chave])

pessoa[chave] = "João"
print(pessoa["nome"])

#if pessoa.get("sobrenome", None) :  Não existe
#if pessoa.get("sobrenome", "Não existe"):
