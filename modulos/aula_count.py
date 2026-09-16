# count() -> um contador infinito;
# se não setar um break ele fica infinito
# possivel usar argumentos nomeados - > start e step
# start -> iniciar 
# step -> passos

from itertools import count

infinito = count(start=5, step=10) # não importa a ordem dos args

print("count")

for i in infinito:
    print(i)
    if i > 50:
        break

# range() -> um contador finito;
# range(start, finish, step)
# 1, 11, vai a 10.

finito = range(5, 56, 10)

print("\nrange")

for f in finito:
    print(f)

