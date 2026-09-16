# Decorando e decorador de funções.
# Syntax Sugar # @\
# Decorar uma função, seria uma closure, que pode Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python 
# usar as funções decoradoras em outras funções. 
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def exec(func): # Executar a função invert_string 
    print("Vou te decorar")
    def inner(*args, **kwargs): # Aqui pega os parametros da função invert_string
        for arg in args: # Passa de um por um, pelo param de invert string, o texto
            is_string(arg) # chama is string, e dentro o parametro
        resultado = func(*args, **kwargs) # func = invert_string e os argumentos é a string
        print(f'O seu resultado foi {resultado}.') # resultado
        print('Ok, agora você foi decorada') 
        return resultado # e a função retorna o resultado
    return inner

@exec # Decorador
def invert_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError("Digita um texto")

print(invert_string("ana"))