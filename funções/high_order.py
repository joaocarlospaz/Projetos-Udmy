"""
Funções de primeira classe
Higher Order Functions e First-Class Functions
Higher Order Functions - Funções que podem receber e/ou retornar outras funções
First-Class Functions - Funções que são tratadas como outros tipos de dados comuns 
(strings, inteiros, etc...)
"""

def saudacao(msg, nome): # Pode ser parametros
    return f"{msg}, {nome}!"

def executa(funcao, *args): # Usando uma função dentro de outra função
    return funcao(*args)


print(
    executa(saudacao, "Bom dia", "Luiz")
)
