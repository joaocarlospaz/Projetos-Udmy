import json

CAMINHO = "C:\\Users\\N1no\\OneDrive\\Documentos\\Projetos Udmy\\aulas_json\\sim.json"

lista = []

with open(CAMINHO, "w", encoding= "utf-8") as arquivo:
    json.dump(
        lista,
        arquivo,
        indent=2,
        ensure_ascii=False,
    )

with open(CAMINHO, "r", encoding= "utf-8") as arquivo:
    arquivo.seek(0, 0)
    lista = json.load(arquivo)
    


print(lista)

