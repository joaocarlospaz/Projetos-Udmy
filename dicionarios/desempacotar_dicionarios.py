# Formas de desempacotar dicionarios!!!!!!!!

# (a1, a2), (b1, b2) = pessoa.items()
# print(f"{a1}: {a2} {b2}") Desempacotando com vareavéis

# for chaves, itens in pessoa.items(): # SEMPRE ESPECIFIQUE O QUE VOCÊ QUER DO DICIONARIO BRO
#     print(chaves, itens)
# PARA EXTRARIR UM DICIONARIO USA DOIS ASTERISCOS **
pessoa = {
    "Nome": "Glória",
    "Sobrenome": "Kaline",
}

dados_pessoais = {
    "Idade": 20,
    "Sexo": "Feminino",
}


# *args e **kwargs
# *args já vimos args.py
# **kwargs keyword arguments (argumentos nomeados)
pessoa_completa = {**pessoa, **dados_pessoais}
print(pessoa_completa)
print()

def mostrar_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items(): # Argumentos nomeados
    
        print(chave, valor)
    for i in args: # Argumentos não nomeados
        print(i)
mostrar_argumentos_nomeados(1, 2, 3, Nome="Nobru", Freefire="Garena")
mostrar_argumentos_nomeados(**pessoa_completa) 


