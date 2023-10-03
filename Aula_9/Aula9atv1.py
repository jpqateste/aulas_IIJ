import pandas as pd

data = {
    'Nome': ['Davi', "Maria", "Monica", "João", "Camila", "Luciana", "Patricia"],
    'Idade': [51, 37, 23,24, 33, 18, 22,],
    'cidade' :["Recife", "Recife", "Recife", "Salvador", "Salvador", "Salvador", "São Paulo"]
}

df = pd.DataFrame(data)

print(df[df['cidade']== "Recife"])

df.to_csv("pasta1/minhaprimeiratabela.csv")