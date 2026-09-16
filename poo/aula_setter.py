# aula de @setter
# p/ ter um setter precisamos de um getter
# p/ evitar quebra de código
# Você controla o que pode entrar no atributo.

class Caneta:
    def __init__(self, cor):
        self._cor = cor # arderline antes, para dizer pra ngm usar, apenas eu
        print("setter")
        self.tampa = None

    @property
    def cor(self):
        return f"Caneta {self._cor}"

    @cor.setter # setter recebe self, e um parametro para receber valor
    def cor(self, valor): 
        self._cor = valor 

    @property
    def cor_tampa(self):
        return f"cor da tampa {self.tampa}"

    @cor_tampa.setter
    def cor_tampa(self, tampa):
        self.tampa = tampa
        

caneta = Caneta("Azul")
print(caneta.cor)
caneta.cor = "Preta"
print(caneta.cor)

print(caneta.cor_tampa)
caneta.cor_tampa = "Black"
print(caneta.cor_tampa)

