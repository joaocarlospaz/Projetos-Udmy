# Gerador de senhas.py
import random
import string

def gerador_senhas(tamanho):
    caracteres = (
        string.ascii_letters +
        string.digits +
        "!@#$%&*"  
    )
    senha = ""
    for _ in range(tamanho):
        senha += random.choice(caracteres)
    return senha

tamanho = int(input("Qual o tamanho da sua senha? "))
senha = gerador_senhas(tamanho)
print(f"Senha Gerada: {senha}")
