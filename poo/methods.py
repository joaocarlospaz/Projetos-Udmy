# Três tipos de métodos
# Method vs @classmethod vs @staticmethod
# method -> usa a instância da classe (self)
# @classmethod -> usa a classe como instância (cls)
# @staticmethod -> isola a função

# Method
class Professor:
    def __init__(cls, nome, materia):
        cls.nome = nome
        cls.materia = materia 

    @classmethod
    def apresentacao(cls, nome, materia): 
        professor = cls
        professor.nome = nome
        professor.materia = materia
        return f"Olá, sou {professor.nome} e vou lecionar {professor.materia};"

# p1 = Professor("João", "Inglês")
# print(p1.apresentacao())
# print()

# @classmethod
# Maneira diferente de atribuir valores
print(Professor.apresentacao("João", "Inglês"))

# @staticmethod
# Metodo que é uma função dentro da classe, fim...
# Não tem acesso ao self nem ao cls


