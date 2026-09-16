"""
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno.
""" 
# Criando um set
# set(iterável) ou {1, 2, 3}

# s1 = set("Luiz") # Aleatorio
# for s in s1:
#     print(s)
# print(s1)

# s1 = {"Luiz", 1, 2, 3} set com dados, garante conformidade.
# print(s1)

# s1 = set() # vazio
# s1 = {"Luiz", 1, 2, 3} # Com dados

"""
São muito eficientes para remover valores duplicados de iteraveis;
- Seus valores sempre serão únicos;
- Não aceitam valores mutáveis;
- Não tem indexes;
- Não garantem ordem;
São iteráveis (for, in, not in)
"""
# ↓

# s1 = {1, 2, 3 , 3, 3, 3, 3, 1}
# print(s1)
# print(3 in s1)
# print(3 not in s1)

# Método úteis:
# add, update, clear, discard

s1 = set()
s1.add(1)
s1.add("Luiz")
print(s1)
s1.update(("Olá mundo", 1, 2, 3, 4))
print(s1)
# s1.clear() # Limpar
s1.discard("Olá mundo") # Descarta um valor do set
print(s1)
print()
# Operadores importantes
# união | union - Une
# Intersecção & intersection - Itens presentes em ambos
# Diferença - Itens presentes apenas no set da esquerda
# Diferença simétrieca ^- Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2
print(s3)
print(s4)
print(s5)
print(s6)


