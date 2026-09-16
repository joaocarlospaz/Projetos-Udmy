# isistance -> para saber se é de determinado time
# isinstance(valor, tipo)
lista = [
    "a", 1, 1.5, True, [0, 1, 2], (1, 2),
    {0, 1}, {"nome": "sobrenome"}
]

for item in lista:
    print(item, isinstance(item, set))