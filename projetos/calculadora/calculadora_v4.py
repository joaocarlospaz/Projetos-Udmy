import json
# código de uma calculadora
# Fazer no minimo 4 tipo de operações
# Mostrar a operação
# Salvar em arquivo.json

def soma(x , y):
    return x + y

def subtrair(x , y):
    return x - y

def multiplicar(x , y):
    return x * y

def dividir(x , y):
    return x / y

def ler_numeros():
    x = float(input("\nDigite um número: "))
    y = float(input("Digite outro número: "))
    return x, y

def salvar(resultados, caminho):
    dados = []
    with open(caminho, "w", encoding= "utf-8") as arquivo:
        json.dump(
            resultados,
            arquivo,
            ensure_ascii=False,
            indent=2,
        )
    return dados

def ler(resultados, caminho):
    dados = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não existe!")
        salvar(resultados, caminho)
        dados = resultados
    return dados

resultados = []
CAMINHO = "C:\\Users\\N1no\\OneDrive\\Documentos\\Projetos Udmy\\projetos\\calculadora\\operacoes.json"
ler([], CAMINHO)
operacoes = {
    "+": soma,
    "-": subtrair,
    "x": multiplicar,
    "/": dividir
}

while True:

    print("\nMenu: ")
    escolha = input(
        "+ - Somar\n" 
        "- Subtrair\n" 
        "x - Multiplicar\n" 
        "/ - Dividir\n"
        "c - Limpar\n" 
        "Press qualquer tecla para sair...\n"
        "Escolha: "
    )

    

    comando = operacoes.get(escolha)

    if comando is not None:
        numero1, numero2 = ler_numeros()
        resultado = f"{numero1:.2f} {escolha} {numero2:.2f} = {comando(numero1, numero2)}"
        print(resultado)

        resultados.append(resultado)
        salvar(resultados, CAMINHO)
    else:
        print(
        "Digite uma operação válida.\n" 
        "Você saiu..."
        )
        break