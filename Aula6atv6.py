'''
Desenvolvam um programa que conte quantas vogais (a, e, i, o, u) existem em uma palavra fornecida pelo usuário.

Implementem uma função que receba uma palavra qualquer (string) como entrada.
O programa deve imprimir o número total de vogais na palavra.
Solicitação de Entrada:

Implementem a solicitação de entrada de uma palavra (string).
Contagem de Vogais:

Implemente um loop "for" ou "while" para percorrer cada caractere da palavra.
Verifique se cada caractere é uma vogal (a, e, i, o, u) e conte-as.
Imprima o número total de vogais na palavra.
'''

palavra = input('Digite uma palavra: ')
vogais = ('a','e','i','o','u')
palavra = palavra.lower()
vogalqnt = 0

for p in palavra:
    if p in vogais:
        vogalqnt = vogalqnt + 1

print(f"A quantidade de vogais na palavra {palavra} é {vogalqnt}")

