'''
Na catraca de acesso, haverá uma tela voltada para o cliente. Todos os dias, quando ele passar, 
deve aparecer a mensagem "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"
Quando ele completar 21 identificações seguidas, deve aparecer a mensagem 
"UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ".
Caso o cliente tenha uma certa frequência, mas falte algum dia, quando retornar, deve aparecer 
"QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO."
'''
qt_id_max = 8
qt_id_input = 0
falta = False
matricula_cliente = "123"

while qt_id_input < qt_id_max:
  
  matricula = input("DIGITE SUA MATRICULA PARA ENTRAR: ")
  print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")
  if matricula_cliente == matricula:
    if falta:
      print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
    qt_id_input = qt_id_input + 1
    falta = False
  else: 
    qt_id_input = 0
    falta = True
    

print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ")  
