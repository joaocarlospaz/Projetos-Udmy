def gen1():
    yield 1 
    yield 2
    yield 3

def gen2(): # ou poderia determinar um parametro nele
    yield from gen1() # vaiu retornar dados do gen1
    yield 4
    yield 5 
    yield 6
    
g = gen2()

print(next(g))
print(next(g))
print(next(g))
print(next(g))