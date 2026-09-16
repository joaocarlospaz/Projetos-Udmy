def multiply(*args): # *args, pois vão ser varios argumentos nomeados; (empacotar)
# Dentro da função, vamos fazer a ação de multiplicar e dar o total;
    total = 1 # Quero que mostre o valor total dos produtos;Fora do for;
    for n in args:
        total *= n # para multiplicar cada número entre si, e ja ir somando o resultado total.
    # print(total)
    return total # FORA DO FOR, DENTRO DA FUNÇÃO
    
numbers = 5, 5, 5
print(f"O resultado total é: {multiply(*numbers)}") # desempacotar
