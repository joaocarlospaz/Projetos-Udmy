# Repetir até acertar
# Faça um loop que pergunte uma senha até o usuário digitar “python123”.

tentativas = 1

while True:
    senha = input("Digite sua senha: ")
    senha_correta = "python123"
    if senha == senha_correta:
        print("Senha correta.")
        break
    elif tentativas == 5:
            print("VOCÊ FOI BLOQUEADO!!!")
            break
    else:
        print(f"senha incorreta.\n" \
        f"5 tentativas erradas, bloqueio. {tentativas}")
        tentativas += 1

    
