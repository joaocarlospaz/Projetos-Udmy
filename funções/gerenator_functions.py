from types import GeneratorType

def generator():
    yield 1 # Pausar
    print("continuando...")
    yield 2 # Pausar
    print("Mais uma...")
    yield 3 + 5 # Pausar
    print("cabou")
    return "caboss"

gen = generator() 
for n in gen:
    print(n)

print(isinstance(gen, GeneratorType))

# generator é uma função que pausa