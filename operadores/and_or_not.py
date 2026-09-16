"""
Operadores lógicos
and (e) or (or) not (não)
and - todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
São consideras falsy (que vc já viu):
0 0.0 '' False
Também existe o tipo NOne que é usado para representar um não valor.
"""
entrada = input('[E]entrar [S]air: ')
senha = input('Senha: ')
# if condição, so se for True

senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print('Bem vindo!')
else:
    print('Você saiu!')

# Avaliação de curto circuito
print(True and 1 and False)
senha = 0 or False or 0 or 'abc' or True
print(senha)