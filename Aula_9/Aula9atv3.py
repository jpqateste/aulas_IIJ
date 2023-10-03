'''
Crie uma persona com a biblioteca Faker com nome, idade e cidade. 
Criando o atributo random.int para gerar valores aleatórios para idade.

'''


from faker import Faker
import random

fake = Faker('pt_BR')

nome_completo = fake.name()
idade = random.randint(1, 100)
cidade = fake.city()

print(nome_completo)
print(idade)
print(cidade)

