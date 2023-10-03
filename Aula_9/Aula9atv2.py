'''
Filtre as pessoas levando em consideração os seguintes critérios:

com idade maior que 40 anos
com renda maior de 5 mil
com renda maior de 15 mil
'''
import pandas as pd

df = pd.read_csv('Aula_9/dados_ficticios.csv')



print(df[df['idade'] > 40 ])
print(df[df['renda'] > 5000.00 ])
print(df[df['renda'] > 15000.00 ])
