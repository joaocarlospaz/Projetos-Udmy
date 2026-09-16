# Jogo da palavra secreta;

palavra = 'Raiva'
print('\nSua dica: Emoção.')
tentativas = 0

while True:
    tentativas += 1
    letra = input('Digite uma letra: ')

    if letra != 1:
        print('Digite apenas uma letra.')
    ...