# o primeiro modulo executado se chama __main__
# Você pode importar outro modulo inteiro ou uma parte dele
# assim como um modulo normal
import aula_main # Posso importar assim
from aula_main import soma # Ou assado
# Lembrando que, modulo, tem que estar na mesma pasta (folder), nao pode estar em outra.

print(aula_main.soma(2, 2))
print(soma(2, 2))
print(__name__)
# Se precisar recarregar o modulo usar, import importlib
# porque, tipo assim, eu nao consigo pegar varios import do codigo, so se for usando 
# importlib.reload(nome_modulo) que vai recarregar o modulo para usar novamente
