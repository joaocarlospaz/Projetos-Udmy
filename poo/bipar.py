# Declaração de classe
class Bip(): 
    def __init__(self, nome, tamanho, estado=False): # Metódo construtor
        # atributos da classe
        self.nome = nome
        self.tamanho = tamanho
        self.estado = estado

    # Metódos da classe
    def bipando(self):
        if self.estado:
            return f"{self.nome} está bipando com o bip {self.tamanho}"

        return f"{self.nome} não está bipando com o bip {self.tamanho}"

    

# Declaração da instância da classe
bip1 = Bip("João", "Pequeno")
bip2 = Bip("Pedro", "Grande", True)
print(bip1.bipando())
print(bip2.bipando())



        