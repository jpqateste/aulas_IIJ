'''
Crie a estrutura de uma tabuada para um valor inserido. 
O resultado deverá ser printado do valor multiplicado de 1 a 10.
'''
numero = int(input("Digite o valor: "))
print("TABUADO DE " + str(numero))

for i in range(1,11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
