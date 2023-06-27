c1 = 50
c14 = 10
cont = 0
cont2 = 0
c3 = 0
c4 = 0
result = 0
num = int(input("Reais a sacar : "))
print("Com esse dinheiro você poderá sacar...")
if num >= 50:
    if c1 >= 50:
        c1 = num / 50
        c12 = int(c1)
        rest = 50 * int(c1)
        result = num - rest

        print(F"Total de {c12} cédulas de 50R$ ")
    if result <= 50 and result >= 10:
        c2 = result / 10
        c22 = int(c2)
        rest = 10 * int(c2)
        result = result - rest

        print(F"Total de {c22} cédulas de 10R$ ")
    if result <= 10 and result >= 5:
        c3 = result / 5
        c32 = int(c3)
        rest = 5 * int(c3)
        result = result - rest

        print(F"Total de {c32} cédulas de 5R$ ")
    if result <= 5 and result >= 1:
        c4 = result / 1
        c42 = int(c4)
        rest = 1 * int(c4)
        result = result - rest
        print(F"Total de {c42} cédulas de 1R$ ")
elif num <= 50:
    if c14 >= 10 and c14 < 50:
        c14 = num / 10
        c142 = int(c14)
        rest = 10 * int(c14)
        result = num - rest
        if num >= 10:
            print(F"Total de {c142} cédulas de 10R$ ")
    if result <= 10 and result >= 5:
        c2 = result / 5
        c22 = int(c2)
        rest = 5 * int(c2)
        result = result - rest

        print(F"Total de {c22} cédulas de 5R$ ")
    if result <= 5 and result >= 1:
        c3 = result / 1
        c32 = int(c3)
        rest = 1 * int(c3)
        result = result - rest

        print(F"Total de {c32} cédulas de 1R$ ")
