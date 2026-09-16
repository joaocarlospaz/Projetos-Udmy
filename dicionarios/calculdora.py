def soma(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def ler_numeros():
    x = int(input("\nDigite um número: "))
    y = int(input("Digite um número: "))
    return x, y

def invalido():
    print("opção invalida!")

operacoes = {
    "1": soma,
    "2": subtrair,
}

opcao = input(
        "\n1) Soma\n" \
        "2) Subtrair\n" \
        "Escolha uma opção: "
)

num_1, num_2 = ler_numeros()

comando = operacoes.get(opcao, invalido)

comando()
