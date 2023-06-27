import datetime
Ano = datetime.date.today().year
cont = 0
cont2 = 0
for pessoa in range(0,7):
    Ano_Nascimento = int(input("Ano de nascimento : "))
    if Ano - Ano_Nascimento >= 21:
        cont += 1
    if Ano - Ano_Nascimento < 21:
        cont2 += 1

print(f"Ao todo tivemos {cont} pessoas maiores de idade.")
print(f"Foram registradas {cont2} pessoas menores de idade.")


