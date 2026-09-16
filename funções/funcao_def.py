"""
Introduções às funções (def) em Python
Funções são trechos de código usados para replicar
determinada ação ao longo do seu código.
Elas podem recebber valores para parâmetros (Argumentos)
e retornar um valor especifico.
Por padrão, funções Python retornam None(nada).
"""

# def Print(a, b , c): # Pode ter qualquer coisa e quantas vezes quiser.

# Print()

# def imprimir(a, b, c): # parametros
#     print(a, b, c)

# imprimir(1, 2, 3) # argumentos
# imprimir(4, 5, 6)

def saudacao(nome="Sem nome"):
    print(f"Olá, {nome}!")

saudacao("João")
saudacao()