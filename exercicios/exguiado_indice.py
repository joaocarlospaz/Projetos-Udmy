print('Seja Bem Vindo!')
nome = input('Digite o seu nome: ')

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    indice += 1
    novo_nome += f'*{letra}'
    print(novo_nome)

print(f'{novo_nome}*')