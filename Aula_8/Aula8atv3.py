'''
A Loja do Joga Junto conta mais uma vez com a colaboração do seu squad! Desta vez, 
surge a necessidade de desenvolver um programa que analisa o CEP inserido pelo usuário 
e determina se ele é elegível para frete grátis. Para realizar essa tarefa, 
foi definida uma política de frete grátis abrangendo todos os estados das regiões Norte e Nordeste do país.  

Faça um brainstorming com sua equipe sobre o fluxo e requisitos necessários para construção desse programa
Desenvolva o programa
Faça casos de teste para este cenário, documente os testes realizados e insira no Bitrix
Caso seja encontrado algum bug no seu código, documente-o. 
'''

import requests

estados = ['AM','RR','AP','PA','TO','RO','AC','MA','PI','CE','RN','PE','PB','SE','AL','BA']

def verificaCep(cep):
    if not cep.isdigit() or len(cep) != 8:
        return "CEP INVÁLIDO."
    
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    date = response.json()
    estado = date['uf']

    if estado in estados:
      return (f"O CEP É LEGÍVEL PARA FRETE GRÁTIS")
    else:
       return (f"O CEP NÃO É LEGÍVEL PARA FRETE GRÁTIS")
    
cep = input ("DIGITE SEU CEP: ")
resultado = verificaCep(cep)
print(resultado)
