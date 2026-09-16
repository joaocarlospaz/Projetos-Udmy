# try e except
# Pode usar quantos except existir no seu código;
# TypeError -> Erro na tipagem, tratar um int como uma list e etc;
# ZeroDivisionError -> Divisão por zero;
# IndexError -> Quando o indice esta fora do intervalo;
# NameError -> Erro na logica, falta de variavel, print com P maiusculo e etc.
# SyntaxError -> Erro na sintaxe do codigo, não pega no try/exceptl;
a = 1
b = 0
try:
    # i = b[5] # TypeError, não tem como acionar o indice de um inteiro;
    i = "Nobru"[2] # IndexError, quando o indice esta fora do intervalo;   
    print(i) # Esta dentro do intervalo;
    c = a / b # DivisionError, tentando dividir por ZERO;

except ZeroDivisionError as e:
# Se eu não especificar o tipo de erro, ele vai pegar todo tipo de error.     
    print("ZeroDivisionError;")
    print(e) # motivo;
    print(e.__class__.__name__) # Nome do erro;

except NameError:
    print("NameError;")

except (TypeError, IndexError) as error:
# O as é como se eu estivesse criando uma variavel, vai atribuir qual é o meu erro;
# Pode colocar dois tipos de error em apenas um except, apenas adicionando uma tupla; 
    print("TypeError;IndexError;")
    print(error.__class__.__name__) 
    # Se eu utilizar esses dois dunders, vai me informar qual o tipo do erro;
    print(error)


