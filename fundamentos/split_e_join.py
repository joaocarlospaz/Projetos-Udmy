"""
split - divide a str
join - une uma str
strip - cortas os espaços do começo e do fim.
rstrip - direita
lstrip - esquerda
"""

frase = "Olha só, que coisa mais interessante." 
frase_s = frase.split(',') # vai dividir exatamente na virgula. # cria uma lista.
# se deixar vazio, separa nos espaços.

print(frase_s)

frases_unidas = ", ".join(frase_s)
print(frases_unidas)
