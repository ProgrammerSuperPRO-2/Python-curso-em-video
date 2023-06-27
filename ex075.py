num = int(input("Digite um número : ")),int(input("Digite outro número : ")),int(input("Digite outro número : ")),int(input("Digite outro número : "))
contador = num.count(9)
if 3 in num:
 encontrar = num.index(3)
par = 0

for n in num:
    if n %2 == 0:
        par +=1
print("Números pares encontrados :",par)
