# 4 formas de importar modulos
# import, from, as e *
# https://docs.python.org/pt-br/3.14/py-modindex.html
# Acima estão todos os modulos do python

# 1 - import nome_modulo
# vantagens - > você tem o nomespace do modulo 
# desvantagens - > nomes grandes

# import sys (sys é o nomespace)

# print(sys.platform)

# 2 - from nome_modulo import objeto1, objeto2
# vantagens -> nomes pequenos
# desvantagens -> sem a namespace

# from sys import exit, platform

# print(platform)
# exit()

# 3 - a terceira forma é dar apelidos ao nome do modulo
# Pode usar das duas formas acima
# vantagens -> você pode reservar nomes para seu código
# desvantagens - > perde clareza no código
# import nome_modulo as apelido
# 1 -> import sys as s

# print(s.platform) # meu sys virou "s", menos clareza

# from nome_modulo import objeto as apelido
# 2 -> from sys import exit as ex, platform as plat

# print(plat)
# ex()

# 4 seria usando o * (importa todo o modulo)
# má prática - from nome_modulo import *
# vantagens -> importa todo o modulo
# desvantagens -> importa todo o modulo
# from sys import *

# print(platform)