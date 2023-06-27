fator = int(input("Número : "))
numero = 1
cont = fator + 1
ger = []
print("a fatorial de ",end=" ")
for n in range (0,fator):
    cont = cont - 1
    li = cont
    if li > 0:
     print( cont,end = "")
     print(end = " x " if li>1 else " = ")


for número in range(1, fator):
    result = numero * (número+1)
    numero = result

print(result)
