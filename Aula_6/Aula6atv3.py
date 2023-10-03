'''
Agora crie um script para com uma lista de frutas, e outra lista com o nome alergias. 
Insira uma fruta da lista de frutas na lista de alergias. 

Depois crie um for para cada item da lista passar por uma verificação em uma estrutura 
condicional para verificar se está essa fruta está contida na lista de alergias. 
Caso a fruta esteja na lista, imprima na tela o nome dela. 
input("Digite a fruta: ")
'''
frutas = ['Laranja', 'Maça', 'Mamão', 'Melão', 'Acerola']
alergias = ['Acerola', 'Abacaxi', 'Maracuja']

for frutas in frutas:
    if frutas in alergias:
      print(f'A {frutas} está na lista de alergias')