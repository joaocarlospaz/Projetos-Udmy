"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

entrada = "746824890"

nove = entrada[:9]
contagem_regressiva = 10

soma = 0
for digito in nove:
    soma += int(digito) * contagem_regressiva
    contagem_regressiva -= 1
digito = (soma * 10) % 11
digito if digito < 9 else 0

print(digito)
entrada += str(digito)

dez = entrada[:10]
contagem_regressiva = 10

soma = 0
for digito2 in dez:
    soma += int(digito2) * contagem_regressiva
    contagem_regressiva -= 1
digito2 = (soma * 10) % 11
digito2 if digito2 < 9 else 0

print(digito2)
entrada += str(digito2)

print(f"cpf completo: {entrada}")