# Montar palavra letra a letra
# Peça uma palavra e vá montando ela letra por letra, mostrando o progresso:

palavra = input("Digite uma palavra: ")

i = 0
letra = ""
while i < len(palavra):
        letra += palavra[i]
        i += 1
        print(letra)