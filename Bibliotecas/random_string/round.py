import decimal # Entrega exata de numeros decimais.
# se converter em str, da certo, pela bliblioteca decimal.

numero1 = decimal.Decimal("0.1")
numero2 = decimal.Decimal("0.7")
numero3 = numero1 + numero2

print(numero3) # Imprecisão dos numeros flutuantes;
print(f"{numero3:.2f}") # Delimitar casa decimais;
print(round(numero3, 2)) # Mesma função;

