'''
Crie um script com:

Uma função para criar personas, contendo nome, cidade, idade. 
Salve os dados dessas personas em um arquivo CSV.
Suba todos os arquivos para seu repositório.

'''

from faker import Faker
import pandas as pd
import random

fake = Faker('pt_BR')

data = []

for _ in range(10):
    data.append({
        "nome": fake.name(), 
        "idade": random.randint(1, 100), 
        "cidade": fake.city()
    })
    

df = pd.DataFrame(data)

df.to_csv("pasta1/minhatabela2.csv")   