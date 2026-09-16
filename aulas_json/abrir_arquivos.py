import os

# para abrir um arquivo usamos "open()"
caminho_arquivo = "C:\\Users\\N1no\\OneDrive\\Documentos\\Projetos Udmy\\" # -> pwd no terminal
caminho_arquivo += "aula_arquivo.txt"

# arquivo.close()
# arquivo = open(caminho_arquivo, "w") # com x também criaria;
# # Se for abrir com open sempre deixar o close() pronto
# # para não gerar erros no arquivo

# pra nao ter que ficar abrindo e fechando dessa forma, não correr o risco de esquecer
print("write and read (w+, write, read, seek): \n")

# encoding pra definir a codificação de carecteres;
# as vezes a padrão não lê caracteres especiais.

with open(caminho_arquivo, "w+", encoding= "utf-8") as arquivo:
    # porque with abre e fecha sem precisar do close();
    # passar o caminho do arquivo, modo de operação e o encoding, SEMPRE que for trabalhar com arquivo.
    arquivo.write("Atenção!\n")
    arquivo.write("Olá mundo\n")
    arquivo.write("Hello World\n")
    arquivo.seek(0, 0)
    print(arquivo.read())


print("only read (r, read): \n")
with open(caminho_arquivo, "r", encoding= "utf-8") as arquivo:
    print(arquivo.read())

# os.remove(caminho_arquivo) # unlink, apagar o arquivo
os.rename(caminho_arquivo, "arquivo_da_aula.txt") # Troca o nome ou move o arquivo.


# obs * no windowns temos problema se digitar o caminho com apenas uma barra invertida
# a solução seria, digitar com duas barras invertidas \\

# Modos par usar no arquivo
# r(leitura) / w(escrita) / x(criação)
# with(abrir e fechar) / t (modo texto)
# a (adicionar escrita no final do arquivo) / b (binario) 
# + usamos para:
# r+ (leitura), vai dar pra ler e escrever 
# w+ (escrita), vai dar pra escrever e ler
# Metódos uteis
# write, read (ler e escrever)
# writelines(escrever várias linhas)
# seek(mover o curso pro começo) # 0,0
# readline(ler uma linha)
# readlines(ler várias linhas)
# 