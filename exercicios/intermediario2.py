"""
🔵Nível intermediário (mais próximo do que você viu)
1 Primeiro número duplicado
Dada uma lista, retorne o primeiro número que se repete (igual você tava fazendo 👀).
2 Filtrar números
Dada uma lista, retorne só os números pares.
3 Contador de palavras
Dado um texto, conte quantas palavras existem.
"""
# 1
lista_de_lista_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [15, 2, 3, 4, 5, 6, 7, 8, 10, 10]
]

def numero_duplicado(lista_de_inteiros):
    checagem = set()
    for numero in lista_de_inteiros:
        if numero in checagem:
            return numero
        checagem.add(numero)
    return -1
    
for lista in lista_de_lista_de_inteiros:
    print(lista, numero_duplicado(lista))

# 2
lista = [15, 2, 3, 4, 5, 6, 7, 8, 10, 10]

def filtrar_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

print(filtrar_pares(lista))

# 3
texto = "Operadores de String, Python oferece operadores para processar texto (ou seja, valores de string)."

palavras = texto.split()
numero_de_palavras = len(palavras)

print(numero_de_palavras)