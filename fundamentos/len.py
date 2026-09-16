"""
Fatiamento de Strings
012345678 - INDICE
123456789 - CONTAGEM DE CARACTERES (len)
Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
i - inicio 
f - final 
p - passo (Negativo, vai pra tras)
Obs: A função len, retorna a qtd.
de caracteres str
"""
v = 'Olá Mundo'
print(v[5])
print(v[4:9]) # Um número após para mostrar todo.
print(v[4:]) # omitindo o final. ja lê.
print(v[0:9:2]) # Passo pulando dois.
print(v[::-1]) # Vai inverter a str.