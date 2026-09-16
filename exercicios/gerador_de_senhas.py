# Gerador de senhas

# Atender ao tamanho requerido pelo usuario
# Ter letras, números e caracteres especiais
import string
import random


def gerador(tamanho):
    caracteres = (
    string.ascii_letters + string.digits + "!@#$%&*"
    )
    senha = ""
    for _ in range(tamanho):
        senha += random.choice(caracteres)
    return senha

print(gerador(int(14)))