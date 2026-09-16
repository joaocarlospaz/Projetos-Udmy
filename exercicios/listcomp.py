numeros = [-4, -2, 0, 2, 4]
# cria uma nova lista com os valores dobrados
dobro = [x*2 for x in numeros]
# filtra a lista para excluir números negativos
positivos = [x for x in dobro if x >= 0]
print(positivos)
# chama um método em cada elemento
fruta_fresca = [" banana"," uva ","maça "]
frutas = [fruta.strip() for fruta in fruta_fresca]
print(*frutas, sep = "-")
# achatamento de uma lista usando uma compreensão de lista com dois 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
# se quiser usar mais de um argumento, vai ter que ser em tuplas, para nao dar erro.
#ex. (x, y)