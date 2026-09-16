import sys

# Gererator expression, iterables e iterators em python.
iterable = ["Eu", "Tenho", "__iter__"]
iterator = iterable.__iter__() # tem __iter__ e __next__
# Iterator não sabe nada sobre o seu iteravel, apenas o próximo valor.
lista = [n for n in range(10)]
generator = (n for n in range(10))
print(sys.getsizeof(lista)) # Todos os valores na memoria
print(sys.getsizeof(generator)) # Apenas o primeiro valor na memoria
# sys.getsizeof -> para saber o tamanho na memoria
print(generator.__next__())
print(generator.__next__())
# iterator trabalha com __iter__ e __next__


