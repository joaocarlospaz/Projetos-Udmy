frase = 'O Pyton é uma linguaem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossum.'

i = 0
while i < len(frase):
    letra_atual = frase[i]
    qntd = frase.count(letra_atual)

    print(letra_atual)
    i += 1