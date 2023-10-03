'''
A loja "" tem 2000 clientes e quer enviar mensagens nominais a cada um. A mensagem seria a seguinte:

Olá, . Em  você realizou uma compra no valor de R$500,00 e ganhou um desconto de 10% em sua próxima compra. Use o cupom PAULAÉ10.
'''
nome = " PAULA"
sobrenome = " MARTINS"
loja = "ROUPAS SA"
desconto = "10"
mes = "JANEIRO"
valor = 500,00
'''
print("Olá" + nome + sobrenome + ". Em " + mes + " você realizou uma compra no valor de RS" + str(valor) + " e ganhou um desconto de " + str(desconto) + "% em sua próxima compra. Use o cupom " + nome + str(desconto))
'''
n1 = int(input("Digite sua nota 1: "))
n2 = int(input("Digite sua nota 2: "))
soma = str(n1 + n2)

print("Meu nome é " + nome + " minha primeira nota é: " + str(n1) + " e minha segunda nota é: " + str(n2) + " então minha nota final é " + soma )