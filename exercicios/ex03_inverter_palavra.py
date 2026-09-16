# Inverter string
# Peça uma palavra e mostre ela invertida (sem usar slicing [:: -1]).

palavra = input("Digite uma palavra: ")
i = len(palavra) - 1
invertida = ""


while i > 0:
    invertida += palavra[i]
    i -= 1
    
print(f"Sua palavra é {palavra}, invertida fica {invertida}.")