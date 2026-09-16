"""
if / elif / else
elif e else depende do if;
else é sempre o ultimo;
se / mas se / se não
"""
entrada = input('você quer entrar ou sair? ')

if  entrada == 'entrar':
    print('Você entrou no sistema :]')
elif entrada == 'sair':
    print('Você saiu do sistema :[')    
else:
    print('Você não digitou nem entrar e nem sair.')