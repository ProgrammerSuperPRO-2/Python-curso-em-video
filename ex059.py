import sys
maior = 0
menor = 0

while True:
 maior = 0
 menor = 0
 primeiro = int(input("escreva um número : "))
 maior = primeiro
 menor = primeiro
 segundo = int(input("escreva outro número : "))
 if segundo > primeiro:
    maior = segundo
 elif segundo<primeiro:
    menor = segundo
 print('''[ 1 ] Soma
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Fechar programa''')
 while True:
  escolha = int(input("sua opção : "))

  if escolha == 1:
    print(f"a soma entre {primeiro} e {segundo} é : ", primeiro + segundo)
  elif escolha == 2:
    print(f"a multiplicação entre {primeiro} e {segundo} é :", primeiro * segundo)
  elif escolha == 3:
    print(f"o maior número entre {primeiro} e {segundo} é :", maior)
  elif escolha == 4:
     break
  elif escolha == 5:
      sys.exit("Fechando Sistema...")
  else:
      print("ERRO DESCONHECIDO ENCONTRADO!!!")
      continue





