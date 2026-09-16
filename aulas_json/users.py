import json

# Seu programa deve:
print("old: ")
usuarios = [
    {
        "nome": "João",
        "idade": 20
     },
     {
       "nome": "Glória",
       "idade": 20  
     },
]

# Salvar os usuários no JSON.
with open("users.json", "w+", encoding= "utf-8") as arquivo:
    json.dump(
        usuarios,
        arquivo,
        indent=2,
        ensure_ascii=False,
    )

# Ler o JSON.
with open("users.json", "r", encoding= "utf-8") as arquivo:
    usuarios = json.load(arquivo)
    print(*usuarios, sep="\n")

# Adicionar um terceiro usuário.
with open("users.json", "w+", encoding= "utf-8") as arquivo:
    usuarios.append(dict(nome = "Samara", idade = 19))
# Salvar novamente.
    arquivo.seek(0)
    json.dump(
        usuarios, 
        arquivo,
        indent=2,
        ensure_ascii=False,
    )
    usuarios = json.load(arquivo)
    print(usuarios)

# Ler novamente e imprimir todos.


