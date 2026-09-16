import json
# Salve sua classe em json
# Depois puxe os dados do json em outro file

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
p1 = Pessoa("João", 20)
dados = p1.__getstate__()


CAMINHO_ARQUIVO = r"C:\\Users\\N1no\\OneDrive\\Documentos\\Projetos Udmy\\poo\\exercicio\\dados.json"

with open(CAMINHO_ARQUIVO, "w", encoding= "utf-8") as arquivo:
    json.dump(
        dados,
        arquivo,
        ensure_ascii= False,
        indent=2
    )
