# Função sem lambda:
# def multiplicar(numero, multiplicador):
#     multiplicacao = numero * multiplicador
#     return print(multiplicacao)
# multiplicar(2, 5)

# Porém, temos que ter uma função para executar a função lambda, só jogar na linha
# é mau habito.
# Função com lambda:

def executar(funcao, *args):
    return funcao(*args)
multiplicacao = executar(lambda numero, multiplicador: numero * multiplicador,
                         2, 2)  
# com lambda fazemos toda função em uma única expressão.
# Mesmos resultados, códigos diferentes.

print(multiplicacao)

print(executar(lambda *args: sum(args),
               1, 2, 3, 4, 5))



    
