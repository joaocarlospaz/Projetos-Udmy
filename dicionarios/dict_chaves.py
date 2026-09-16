dicionario = {
    "Nome": "João",
    "Idade": "20",
    "Trabalho": "Logística",
    "Objetivo": "Ganhar dinheiro",
} 

print(f"{dicionario['Nome']}, esse é meu nome :)")
print(f"Tenho {dicionario['Idade']} anos de idade, trabalho com {dicionario['Trabalho']}.")
print(f"Meu objetivo como profissional é {dicionario['Objetivo']}.")
print()
# print(f"Vou fazer uns testes, meu nome e idade é {dicionario['Nome', 'Idade']}")
print("Quantidade de chaves no meu 'dict'", len(dicionario))
print()

print("Apenas as chaves do meu 'dict'", dicionario.keys())
vogais = ["a", "b", "c", "d"]
for chaves, i in zip(dicionario.keys(), vogais): # Junta duas listas e da o valor separadamente
        print(f"{i}) {chaves}")
