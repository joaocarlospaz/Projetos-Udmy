# Menu de cores
def azul():  
    return print("\nVocê escolheu azul !")
def verde():
    return print("\nVocê escolheu verde !")

def amarelo():
    return print("\nVocê escolheu amarelo !")

def quebrar():
    print("\nAté mais!")
    raise SystemExit

def invalido():
    print("\nOpção inválida")

cores = {
    "1": azul,
    "2": verde,
    "3": amarelo,
    "4": quebrar,
}

while True:
    opcao = (
        input(
            "\n1. Azul\n"
            "2. Verde\n"
            "3. Amarelo\n"
            "4. Sair\n"
            "Digite a opção: "
    )
)

    comando = cores.get(opcao, invalido)
    comando()

