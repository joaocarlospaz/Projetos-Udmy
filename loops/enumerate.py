# enumerate é uma função para enumerar os itens de um iteravel.
# lista_enumerada = enumerate(nomes) # vai aparecer o local na memoria.
# lista_enumerada = enumerate(nomes, start = 10) começa do dez.
# nomes.append("Junior") # tuplas são imutaveis.
nomes = ("João", "Carlos", "Paz") 

for a, b in enumerate(nomes):
    # a, b = nome # empacotamento;
    print(a, b)