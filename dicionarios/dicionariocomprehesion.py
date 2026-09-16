player = {"player": "sacy",
          "Seleção": "Brasil",
          "Time": "MIBR"}

info = {
        chave: valor.upper()
        if isinstance(valor, (str, int)) else valor
        for chave, valor 
        in player.items()
}
print(info)


s1 = {2 ** i for i in range(11)}
print(s1)