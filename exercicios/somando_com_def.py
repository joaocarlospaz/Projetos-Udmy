def soma(*args):
    total = 0
    for number in args:
        total += number
    print(f"O total da sua soma é {total}.")
    return total
numbers = [] # Fora do while
while True:
    digitou = input("Digite 's' para digitar o número; \n" \
    "Ou, qualquer outra tecla para mostrar o resultado: ")
    if digitou == "s":
        number_digit = int(input("Número: ")) # int diretamente no número
        numbers.append(number_digit)
    else:
        break

soma(*numbers)

