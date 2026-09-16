import json 

# json serve para armazenar dados simples:

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

# with open('aula117.json', 'w', encoding='utf8') as arquivo:
#     # da mesma forma que um txt, mudando apenas para json
#     json.dump(
#         pessoa,
#         arquivo,
#         ensure_ascii=False, # para mostrar com acentos e etc
#         indent=2, # para organizar o código
#     )

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo) # vai pegar tudo que já foi salvo no arquivo
    print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])