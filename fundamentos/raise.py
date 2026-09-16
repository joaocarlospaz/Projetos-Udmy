def dividir(n, d):
    if not isinstance(n, int):
        raise TypeError (f"({n}) - Deve ser um número inteiro.")
    
        
dividir(5.5, 7)

# raise cria o erro, é meio redundante, porque já daria erro.
