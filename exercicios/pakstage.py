# Se eu quiser importar algo que não esteja na mesma pasta que a minha
# Sem usar sys.path
# O MAIN TEM QUE ESTAR NA RAIZ, PARA PODER UTILIZAR ESSE METODO

# import modulos.modulo # Entra na pasta, entra no modulo
# from modulos import modulo # Entra na pasta, importa o modulo
# from modulos.modulo import * 
# # from exercicios.modulo import soma

# print(modulo.soma(2, 1)) # usando from
# print(modulos.modulo.soma(2, 1)) # usando import
# # print(soma()) # usando from, mas pegando só a soma
# print(variavel)

# PONTO DE VISTA DO MAIN
# Tudo que eu for importar, tem que estar no ponto de vista do meu main

import modulos

print(modulos.dobrar(2))
