# conta bancaria

# Regras:
# Não permitir depósito negativo.
# Não permitir saque maior que o saldo.
# O saldo deve ser acessado através de @property.
# Use _saldo internamente.


class ContaBancaria:
    def __init__(self, nome, id, valor = 0):
        self.nome = nome
        self.id = id
        self._saldo = valor

    @property
    def saldo(self):
        return self._saldo
    
    def __str__(self):
        return f"Olá, {self.nome}({self.id}), seu saldo atual é de {self._saldo}."
    
    def deposito(self, valor):
        if valor <= 0:
            raise ValueError ("Não pode ser negativo")
        else:
            self._saldo += valor
            print(f"Você efetuou um deposito de {valor}")
        return f"Saldo atual: {self._saldo}"
    
    def saque(self, valor):
        if valor > self._saldo:
            raise ValueError ("Saque maior que tudo")
        else:
            self._saldo -= valor
            print(f"Você efetuou um saque de {valor}")
        return f"Saldo atual: {self._saldo}"
    
    def transferir(self, outra_conta, valor):
        if valor <= 0 :
            raise ValueError ("Negativo")
        else:    
            self.saque(valor)
            outra_conta.deposito(valor)

c1 = ContaBancaria("João", "4022", 2_000)
c2 = ContaBancaria("Maria", "0244", 2_000)


print(c1.transferir(c2, 500))
print(f"{c1}\n{c2}")

print()
# saque
print(c1) # saldo atual
print(c1.saque(500)) # saque
# print(c1.saque(2000)) barrado, saque maior que tudo

print()

print("deposito:")
# deposito
print(c1) # saldo atual
print(c1.deposito(3_500)) # deposito 
# print(c1.deposito(-100)) barrado, deposito

