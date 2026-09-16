# Lista de números ao quadrado

# Crie uma lista com os números de 1 até 10, mas com cada número elevado ao quadrado.

quadrados_pares = [n ** 2 for n in range(1, 11) if (n ** 2) % 2==0]
# [valor for item in iterável if condição]
#  [n ** 2      for n in range(1, 11)     if (n ** 2) % 2 == 0]
#    ↑                ↑                          ↑
#  valor        loop (for)                  condição

print(quadrados_pares)
