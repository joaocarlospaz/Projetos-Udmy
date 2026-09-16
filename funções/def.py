
def soma(x, y, z): # parametros, +- uma variavel
    print(f"{x=} {y=} {z=} | x + y + z =",  x + y + z) 

soma(1, 2, 3) # argumentos
# Ou eu posso definir os parametros.
soma(y= 1, x= 3, z= 2) # parametros + argumentos
# a partir do momento que eu defino um parametro no argumento
# eu tenho que usar no restante.
soma(1, z= 2, y= 3) 
# 1 = Argumento posicional e o z = 2 argumento nomeado
