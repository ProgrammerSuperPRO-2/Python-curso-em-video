soma = 0
cont = 0
for n in range(0, 6):
    num = int(input("digite um número : "))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1

print(f"a soma desses {cont} valores é :",soma)
