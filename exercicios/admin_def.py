# O programa pode funcionar assim:
# Digite o usuário: admin
# Digite a senha: 1234
# Saída:
# Login realizado com sucesso

def login(usuario, senha):
    usuario = input("Usuário:")
    senha = input("Senha:")
    print("Login realizado com sucesso") if usuario == "admim" and senha == "1234" else print("Login incorreto")

login(usuario= "admim", senha= "1234")