número = int(input(" Número : "))
div = número/número
div = int(div)
cont = 0

for números in range(div,(número+1)):
    if número%números==0:
      print(f"\33[33m {números}", end='')
      cont = cont+1
    else:
        print(f"\33[31m {números}", end='')
if cont<=2:
          print(f"\33[37m\n{número} só é divísivel por 1 e por ele mesmo;portanto, primo.")
else:
          print(f"\33[37m\n{número} é divísivel por {cont} números; portanto, não é primo.")


