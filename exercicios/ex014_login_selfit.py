print('Seja bem vindo a academia Selfit')

condicao = input('É sua primeira vez aqui?  ')

if condicao == 'não':
    print('Certo, me informe seus dados cadastrais: ')
    cpf = input('CPF: ')
    senha = input('Sua senha: ')

    if senha == '190884Sandra!':
        print('Seja bem vindo de volta, João Carlos!')
    else:
        print('Senha inválida.')
else:
    print('Seja bem vindo ao seu primeiro login!')
    print('Me informe seus dados, para realizarmos seu cadastro: ')
    cpf = input('CPF: ')
    nome = input('Nome Completo: ')
    senha1 = input('Crie uma senha: ')
    dados = (cpf, nome , senha1)
    print(f'Seus dados são: {dados}. Seja Bem Vindo a nossa academia!')
    

