"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e o local,
O escopo Global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 1 # Escopo externo, ja está fora do bloco
# Global
def escopo(): #escopo, esse bloco da função
    def outra_funcao(): #como se cria-se seu proprio mundo
        y = 2 # Só posso usar nesse bloco;
        print(x, y)# x = 1
    print(x)
    # Interno

# print(x)
# Vai dar erro, porque a função não tem
# nada ver com o de fora do bloco

    outra_funcao() 
escopo()

# x = 1 da erro, pois está depois do bloco
# Cada função tem o seu escopo;
# call stack - local para guardar dados
# pilha de chamadas
