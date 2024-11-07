import pandas as pd
import numpy as np
import random


def gerador_de_id_unico():
    while True:
        id_novo = random.randint(10000, 99999) 
        if id_novo not in ids_existentes:
            ids_existentes.add(id_novo)
            return id_novo

df = pd.read_excel("Tabela de vendas.xlsx")
id_coluna = "CustomerID"
ids_existentes = set(df[id_coluna].dropna().astype(int)) 

df[id_coluna] = df[id_coluna].apply(lambda x: gerador_de_id_unico() if pd.isna(x) else x)
df.to_excel("planilha_atualizada.xlsx", index=False)
