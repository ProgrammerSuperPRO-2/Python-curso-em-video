import datetime
ano = int(input("ano do nascimento : "))
ano_atual = datetime.date.today().year
idade = ano_atual - ano

if idade <= 9:
    print(f"o atleta tem {idade} anos")
    print("Categoria MIRIM")
elif 14 >= idade > 9:
    print(f"o atleta tem {idade} anos")
    print("Categoria INFANTIL")
elif 19 >= idade > 14:
    print(f"o atleta tem {idade} anos")
    print("Categoria JÚNIOR")
elif 25 >= idade > 19:
    print(f"o atleta tem {idade} anos")
    print("Categoria SÊNIOR")
elif idade > 25:
    print(f"o atleta tem {idade} anos")
    print("Categoria MASTER")