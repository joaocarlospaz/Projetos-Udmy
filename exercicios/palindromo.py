def verificando_palindromo(texto):
    string = texto.replace(" ", "").lower()
    palindromo = string[::-1]

    return string == palindromo


print(
    verificando_palindromo(
        "Socorram me subi no onibus em Marrocos"
        )
    )

