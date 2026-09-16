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
# import re
import sys
import random
for _ in range(10):
    cpf = ""
    for i in range(9):
        cpf += str(random.randint(0,9))
# entrada = input("Digite o seu cpf: ")
# # cpf = "718.804.434.".replace(".", "").replace("-", "")
# cpf = re.sub(
#     r"[^0-9]",
#     "",
#     "718.djaufosioiasd804.434"
# ) # so pega os numeros;

# entrada_sequencial = entrada == entrada[0] * len(entrada)

# if entrada_sequencial:
#     print("Você enviou dados sequenciais.")
#     sys.exit()
    nove_digitos = cpf[:9] # pegando do primeiro numero ate o nono.
    contagem_regressiva1 = 10

    resultado_digito1 = 0
    for digito in nove_digitos:
        resultado_digito1 += int(digito) * contagem_regressiva1
        contagem_regressiva1 -= 1 # vai subtrair um.
    digito = (resultado_digito1 * 10) % 11 # fora do for
    digito = digito if digito <=9 else 0 # fora do for
    # print(digito) # fora do for
    cpf += str(digito)

    dez_digitos = cpf[:10]
    contagem_regressiva2 = 11

    resultado_digito2 = 0
    for digito in dez_digitos:
        resultado_digito2 += (int(digito) * contagem_regressiva2)
        contagem_regressiva2 -=1
    digito2 = (resultado_digito2 * 10) % 11
    digito2 = digito2 if digito2 <=9 else 0 
    #         Valor     Condição    Outro valor
    # print(digito2)
    cpf += str(digito2)
    cpf_total = cpf
    print(cpf_total)

    verificacao = "Valido" if cpf == cpf_total else "Invalido"
    print(verificacao)