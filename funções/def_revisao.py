def saudacao(nome):
    print("Olá", nome)

saudacao("João")

def soma(a, b):
    print("Soma:", a + b)

soma(5, 7)
soma(a= 5, b= 7)

def dados(nome, idade= None):
    print(f"nome:{nome}, idade:{idade}" if idade else f"{nome} não informou a idade.")

dados("João", 19)
dados("João")
