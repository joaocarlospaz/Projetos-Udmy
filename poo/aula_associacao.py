# Geralmente temos uma associação quando um objeto
# tem um atributo que referência outro objeto
# Associação é um tipo de ligação entre objetos
# mais simples

class Escritor():
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, nome):
        self._ferramenta = nome

class FerramentaEscrever():
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f"{self.nome} está escrevendo"        

escritor = Escritor("João")
caneta = FerramentaEscrever("caneta")
print(caneta.escrever())
escritor.ferramenta = caneta # associação
print(escritor.ferramenta.escrever()) 

