# def dentro(x):
#     a = x # Variavel livre, posso acessar de outras funções
#     # a + b # b is not definned
#     def fora():
#         # b = 0 varivel local
#         return a 
#     return fora

# dentro1 = dentro(10)
# dentro2 = dentro(20)

# print(dentro1())
# print(dentro2())

def texto(string):
    valor_final = string
    def concatenar(valor_a_concatenar):
        nonlocal valor_final # Pra dizer que essa variavel nao é local e sim livre
        valor_final += valor_a_concatenar # não da para alterar uma variavel livre que esta fora do escopo
        # por ter a mesma nomenclatura
        return valor_final
    return concatenar

valor = texto("a") # string
valor("b") # valor_a_concatenar
valor("c") # valor_a_concatenar
valor("d") # valor_a_concatenar
final = valor("") # se deixar sem nada, não vai pegar, pois tem um argumento na função
print(final)

# Variável livre → ler uma variável do escopo externo.
# nonlocal → modificar essa variável do escopo externo.