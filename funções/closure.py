"""
Closure e Funções que retornam outras funções
"""

def saudacao(saudacao):
    def saudar(nome): # saudacacao vai ser lembrada, mas nome nao
        return f"{saudacao}, {nome}!"
    return saudar # se eu deixar sem parenteses, so vai guardar na memoria;


falar_bom_dia = saudacao("Bom dia")
falar_boa_noite = saudacao("Boa Noite")

print(falar_bom_dia("João")) # Aqui, eu to executando a função
print(falar_boa_noite("João")) # Aqui também, isso é closure;

