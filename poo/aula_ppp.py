# Encapsulamento - Aula sobre public, protected e private
# POR CONVENÇÃO 
# (sem underline) public:
# pode ser usado em qualquer lugar

# (com 1 underline) protected: 
# pode apenas ser usada na classe
# e nas suas subclasses.

# (com 2 underlines) private:
# name magling -> desconfiguração de nome
# DEVE ser usada, apenas na classe de origem.

class Encapsulamento:
    def __init__(self):
        self.public = "Isso é publico"
        self._protected = "Isso é protected"
        self.__private = "Isso é privado"

    def method_public(self):
        return self.public
    def _method_protected(self):
        return self._protected
    def __method_private(self):
        return self.__private

enc = Encapsulamento()

print(enc.method_public()) # publico
# print(enc._protected) # Não deve ser usado fora da classe/subclasse;
# print(enc._method_protected()) 

# print(enc._Encapsulamento__private) # Não deve ser usado fora da classe;
# print(enc_Encapsulamento__private) # name magling