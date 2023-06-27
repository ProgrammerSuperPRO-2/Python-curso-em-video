coluna1 = []
coluna2 = []
coluna3 = []
soma_coluna = 0
maior = 0
pares = 0
c = 0
a = int(input("colunas : "))
for espaços in range(0,a):

        valor = int(input(f"matriz [0,{espaços}] : "))
        coluna1.append(valor)

for espaços in range(0, a):
            valor = int(input(f"matriz [1,{espaços}] : "))
            coluna2.append(valor)

for espaços in range(0, a):
            valor = int(input(f"matriz [2,{espaços}] : "))
            coluna3.append(valor)

print("\n")
for elementos in coluna1:
   print(f"[ {elementos:^5} ]",end=" ")

print("\n")
for elementos in coluna2:
   print(f"[ {elementos:^5} ]",end=" ")

print("\n")

for elementos in coluna3:
   print(f"[ {elementos:^5} ]",end=" ")




