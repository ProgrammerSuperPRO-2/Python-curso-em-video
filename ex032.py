import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
ano2 = date.year


ano = int(input("ano a analisar (0 pata atual) : "))

if ano%400 == 0 or ano%100 != 0 and ano%4 == 0  :
    print("ano bissexto")
elif ano == 0 and ano2%400 or ano%100 != 0 and ano2%4 == 0 :
    print("bissexto")

else:
    print("ano não é bissexto")

