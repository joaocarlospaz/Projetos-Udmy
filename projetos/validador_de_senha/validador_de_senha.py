"""
🟢 Nível 1 — Aquecimento de lógica
1. Validador de senha

Faça um programa que recebe uma senha e verifica se ela é válida.

Regras:

Pelo menos 8 caracteres
Tem pelo menos 1 número
Tem pelo menos 1 letra maiúscula
"""

while True:
    senha = input("Digite uma senha a ser validada: ")
    tem_numero = False # pra fazer um validador, crie marcadores;
    tem_maiusculo = False

    for letra in senha:
        if letra.isdigit():
            tem_numero = True
        if letra.isupper():
            tem_maiusculo = True

    if len(senha) >= 8:
        print("Sua senha deve ter no minimo, 8 caracteres.")
    elif not tem_numero:
        print("Sua senha deve conter no minimo, 1 número.")
    elif not tem_maiusculo:
        print("Sua senha deve conter no minimo, 1 letra maisucula")
    else:
        print("Senha validada!")
        break


  
