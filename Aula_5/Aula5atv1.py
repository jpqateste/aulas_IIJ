'''
USANDO IF: Construa um script para verificar se o usuário tem uma idade maior que 18 anos, se tiver, 
imprima na tela "Indivíduo possui idade mínima para dirigir"
USANDO ELSE: Complemente o script feito, imprimindo na tela 
"Indivíduo NÃO possui idade mínima para dirigir"
USANDO ELIF: Complemente o script feito, imprimindo na tela 
"Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir"
'''
idade_minima = 18
idade = int(input("Digite sua idade: "))

if idade > idade_minima:
    print("Indivíduo possui idade mínima para dirigir")
elif idade >=17 or idade<=18:
    print("Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir")

else: 
    print("Indivíduo NÃO possui idade mínima para dirigir")