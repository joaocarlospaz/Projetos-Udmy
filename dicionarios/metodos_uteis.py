"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefaullt - adiciona valor se a chave não existe
copy - Retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""
p1 = {
    "nome": "João",
    "sobrenome": "Carlos",
}

# p1.update(nome="novo valor", idade= 19)
p1.update({
    "nome": "Nobru",
    "idade": 19,
})
print(p1)                   

tupla = ("nome", "novo valor"),
p1.update(tupla)
print(p1)
d1 = {
    "c1": 1,
    "c2": 2,
    "l1": [0, 1, 2],
}

d2 = d1.copy() # Dois dicionarios separados
# Cópia tudo que for imutavel
print()


d2["c1"] = 1000
d2["l1"][1] = 9999 # For mutavel, continua o mesmo valor em ambas
print(d1) # Não altera o valor do dicionario
print(d2) # Novo dicionario
print()

pessoa = {
    "nome": "João",
    "sobrenome": "Carlos",
    "idade": 900,
}

pessoa.setdefault("idade", 0)
print(pessoa["idade"])
print()

print(len(pessoa))  # Quantas chaves
print()

print(list(pessoa.keys())) # retorna as chaves
print()

print(len(pessoa.values())) # retorna os valores
print()

print(list(pessoa.items())) # retorna os dois
print()

for valor in pessoa.values():
    print(valor)
print()

for chave, valor in pessoa.items():
    print(chave, ":", valor)
print()