'''
O instituto Joga Junto vai checar todos os emails existentes utilizados pelos usuários. 
Para isso sua equipe precisará criar  um código para verificar se o email inserido pelo 
usuário tem o @jogajuntoinstituto.org no texto. 

Crie um input para verificar esse texto.

Crie casos de teste escritos em BDD, um com sucesso, e outro com falha. Execute os testes, 
documente e suba os resultados no Bitrix da sua equipe. 
'''
dominio = '@jogajuntoinstituto.org'
email_check = False

while email_check == False:
  email = input ('Digite seu e-mail: ')
  
  if dominio in email:
    print('E-mail verificado')
    email_check = True
  else:
    print('E-mail não confere')
  