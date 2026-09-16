# @property -> O método age como um atributo da instância da classe.
# property é um getter no modo pythônico
# vantagens:
# impede o cliente de ter que quebrar o código
# p/ habilitar um setter
# p/executar ações ao receber um atributo
# **obs - Código cliente, é o código que usa sua classe

# @ property

class Caneta:
    def __init__(self, cor):
        self.cor_caneta = cor

    @property
    def cor(self): # se eu utilizar property, o metodo age como um atributo
        print("A caneta é: ")
        return self.cor_caneta

caneta = Caneta("Azul")


class Cachorro:
    def __init__(self, som):
        self.latido = som

    def get_latir(self):
            print("cachorro faz: ")
            return self.latido

cachorro = Cachorro("au au")

if __name__ == "__main__":
    print("Usando @property:")
    print(caneta.cor) # Atributo da instância da classe
    print()

    # getter
    
    print("Usando um getter:")
    print(cachorro.get_latir()) # usa o método que retorna o atributo - é um @property
    # impedindo de quebrar o código se houver uma alteração, ou algo do tipo