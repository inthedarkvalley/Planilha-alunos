import pandas as pd 

df = pd.read_csv("notas_alunos.csv", sep=";")
df ["média"] = (df["nota_1"]+df["nota_2"]) /2
df.loc[df["média"] < 7, "situação"] = "Reprovado"
df.loc[df["média"] >= 7, "situação"] = "Aprovado"
df.loc[df["faltas"] >5, "situação"] = "Reprovado"
df.to_csv("alunos_situacao_csv", sep=";")
print(df)
print("o número máximo de faltas foi: "+str(df["faltas"].max()))
print("A média geral das notas dos alunos foi: "+str(df["média"].median()))
print("A maior média entre os alunos foi:" +str(df["média"].max()))
