# Exercise Udemy
nome = input('Digite seu nome: ')
idade = input('Sua idade é: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é: {nome [::-1]}')
    if ' ' in nome:
        print(f'Seu nome tem espaço.')
    else:
        print(f'Seu nome não tem espaços.')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')
else:
    print('Você não digitou nada.')


      

