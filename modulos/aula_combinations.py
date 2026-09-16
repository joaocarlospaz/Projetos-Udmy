# combinatons, permutations and product
# usados para fazer combinações
# metodos do modulo itertools

from itertools import combinations, permutations, product

def execute(param):
    print(
        *list(param), sep="\n"
        )
    print()

names = [
    "João", "Glória", "Amor", "Sim"
    ]

last_name = [
    "Carlos", "kaline", "Vida", "Não"
    ]
    

information = [
    ["Preto", "Branca"],
    ["P", "M", "G"],
    ["Masculino", "Feminino"]
]

union = zip(names, last_name)
# combinations
# combinations não repetem combinações.
# combinations(iteravel, valor_das_combinacoes)
# Ex.: 
# João, Glória não vai repetir mais Glória, João

execute(combinations(union, 2))


# permutations
# permutations permite todas as combinações possiveis
# permutations(iteravel, valor_das_combinacoes)
# Ex.: 
# João, Glória vai usar Glória, João

execute(permutations(names, 2))

# product
# product permite fazer combinações com mais de uma lista
# cresce exponecialmente
# product(iteravel, repeat= x) repeat, para o número de repetições do cód

execute(product(*information))