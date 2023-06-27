coluna1 = []
coluna2 = []
coluna3 = []
soma_coluna = 0
maior = 0
pares = 0
c = 0

for espaços in range(0,3):

        valor = int(input(f"matriz [0,{espaços}] : "))
        coluna1.append(valor)

for espaços in range(0, 3):
            valor = int(input(f"matriz [1,{espaços}] : "))
            coluna2.append(valor)

for espaços in range(0, 3):
            valor = int(input(f"matriz [2,{espaços}] : "))
            coluna3.append(valor)

print("\n")
for c,elementos in enumerate(coluna1):
   if c == 1:
        maior = elementos
   print(f"[ {elementos:^5} ]",end=" ")
   if elementos % 2 == 0:
       pares = elementos + pares
   if c == 2:
       soma_coluna = soma_coluna + elementos

print("\n")

for c,elementos in enumerate(coluna2):
   print(f"[ {elementos:^5} ]",end=" ")
   if elementos % 2 == 0:
       pares = elementos + pares
   if c == 1:
    if elementos > maior:
       maior = elementos
   if c == 2:
       soma_coluna = soma_coluna + elementos

print("\n")

for c, elementos in enumerate(coluna3):
   print(f"[ {elementos:^5} ]",end=" ")
   if elementos % 2 == 0:
       pares = elementos + pares
   if c == 2:
       soma_coluna = soma_coluna + elementos
   if c == 1:
    if elementos > maior:
       maior = elementos

print("\nA soma dos números pares é : ",pares)
print("A soma dos valores da terceira coluna é : ",soma_coluna)
print("O maior valor da segunda colunA é : ",maior)


print(coluna1,coluna2,coluna3)