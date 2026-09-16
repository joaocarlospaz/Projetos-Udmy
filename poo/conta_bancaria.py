from rich import inspect
class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depósitos;
    """
    def __init__(self, nome, id, saldo = 0):
        self.nome = nome
        self.id = id
        self.saldo = saldo

    def __str__(self):
        return f"Conta {self.id} de {self.nome} tem {self.saldo:,.2f}."

    def depositar(self, deposito):
        self.saldo += deposito
        print("Deposito efetuado")

    def sacar(self, saque):
        if saque > self.saldo:
            print(f"Saque maior que saldo, seu saldo atual é de {self.saldo:,.2f}")
        else:
            self.saldo -= saque
            print("Saque efetuado")



c1 = ContaBancaria("João", 111, 3000)
c1.depositar(2000)
print(c1)
print()
c1.sacar(1500)
print(c1)
print()
c1.sacar(3600)
print(c1)
inspect(c1)
print(c1.__getstate__())