"""
imutáveis que vimos: str, int, bool, float.
"""
string = 'João Carlos'

texto = "python"
print("Antes:", texto, id(texto))

texto = texto + "3"
print("Depois:", texto, id(texto))
# O que acontece:
# "python" não muda
# "python3" é outro objeto
# -> Os id() serão diferentes
# String → "abc" → "abcd" (novo objeto)
# Lista → [1,2,3] → [1,2,3,4] (mesmo objeto)