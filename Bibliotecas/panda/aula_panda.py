import panda as pd 

# DataFrame e Series, Tabela ou planinha de excel

dados = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [25, 47, 32]
}
df = pd.DataFrame(dados)    
print(df)
print("===================")
s = pd.Series([10, 20, 30])
print(s)

df = pd.read_excel("Financeiro.xlsx", sheet_name= "Agosto")
print(df)