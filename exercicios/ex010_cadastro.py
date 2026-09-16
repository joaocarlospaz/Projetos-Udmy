# Fazendo tudo que vem na cabeça;
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')


if nome and idade:
    print(f'Seu nome e sua idade são, {nome}, {idade}.')
    sexo = input('Obrigado por baixar nosso app, deixe seu feedback: ')
    senha = input('Certo, agora vamos criar uma senha para o seu login: ')
    senha2 = input('Confirme sua senha, por favor:')

    if senha == senha2:
        print('Senhas verificadas, seja bem vindo!')
        print(f'Bem vindo, {nome}, espero que goste do nosso app!')
        
    else:
        print('Suas senhas não correspodem.')
        
else:
    print('Falta informações.')
