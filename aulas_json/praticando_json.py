import json

usuario = {
    "nome": "João",
    "idade": 18,
    "Estado Civil": "Solteiro"
}

with open("usuario.json", "w", encoding= "utf-8") as arquivo:
    usuario["Sobrenome"] = "Carlos"
    json.dump(
        usuario,
        arquivo,
        indent=2,
        ensure_ascii=False,
    )

    

with open("usuario.json", "r", encoding= "utf-8") as arquivo:
    usuario = json.load(arquivo)
    print(usuario)
    