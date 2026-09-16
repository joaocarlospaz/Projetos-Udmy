# Calculadora com while

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (-+*/): ')

    num_1_float = 0 # Tem que deixar '0' pois vai atribuir um valor a variavel no while.
    num_2_float = 0

    try: # Verificar se está correto mesmo.
        num_1_float = float(numero_1) 
        num_2_float = float(numero_2)
        numeros_validos = True
    except: # Se não estiver correto:
        numeros_validos = None # None = Nenhum

    if numeros_validos is None:
        print('Um ou ambos os números são inválidos. ')
        continue

    operadores_validos = '+-*/'

    if operador not in operadores_validos: # not in (não está entre.) 
        print('Operador inválido. ')
        continue

    if len(operador) > 1: # Se digitar mais de um, vai dar erro.
        print('Digite apenas um operador. ')
        continue

    print('Confira o seu resultado abaixo: ')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ',num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ',num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ',num_1_float / num_2_float)
    else:
        print('Isso nunca deveria acontecer. ')

    sair = input('Você quer sair ? ("s") ou ("n"): ').lower().startswith('s')
    print(sair) # .lower() = tudo minusculo , .startwith('s') = começa com ('')

    if sair is True:
        print('Você saiu !')
        break
