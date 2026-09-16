# Sistemas de perguntas e respostas...

perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "2", "3", "4", "5"],
        "Resposta": "4",
},
{
    "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"], # Lista de 3 dicionarios
        "Resposta": "25",
},
{
    "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
},
] 
qtd_acertos = 0 # Quantidade de acertos fora do for, pra nao reiniciar a contagem sempre.
for pergunta in perguntas: # Pega um dicionario por vez de dentro da lista (perguntas).
    print(f"Pergunta: {pergunta['Pergunta']}") # Pegando apenas as perguntas de cada dict.
    print() # Como se fosse um quebra linha

    opcoes = pergunta["Opções"] # Variavel pegando apenas as Opções do dicionario.
    for i, opcao in enumerate(opcoes): # Enumerando e pegando as opções de um por um.
        print(f"{i}) {opcao}") # numero da opcao + opcao.
    
    print() # Como se fosse um quebra linha
    escolha = input("Escolha uma opção: ") # Pergunta, Após apresentar todo os outros blocos,
    # Depois de mostrar a pergunta e as alternativas juntamente das opções.

    acertou = False # Acertou False = errado
    escolha_int = None # Escolha int, não é nenhum valor; nada
    qtd_opcoes = len(opcoes) # numero total de opcoes.
    
    if escolha.isdigit(): # Se for um número inteiro.
        escolha_int = int(escolha) # Converto para int(eiro).

    if escolha_int is not None: # Se não for nada.
        if escolha_int >= 0 and escolha_int < qtd_opcoes: # Se for maior/menor que o número de alternativas.
            if opcoes[escolha_int] == pergunta["Resposta"]: # no caso aqui, eu to pegando o indice dentro de opções
                # e validando se realmente o indice que eu escolhi, bate com a resposta.
                acertou = True # Tudo do bloco confirmado == acertous
    print() # Como se fosse um quebra linha
    if acertou: # se acertou for verdadeiro:
        qtd_acertos += 1 # Se foor verdadeiro, vai somando número de acertos que está fora do for.
        print("Acertou")
    else: # Se acertou for falso
        print("Errou")

print(f"Você acertou {qtd_acertos}")
print(f"de {len(perguntas)} perguntas.")

