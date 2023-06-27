c = 0
lista = [[],[]]
while True:
     c = c+1
     num = int(input(f"Digite o valor {c} : "))
     if num %2 == 0:
         lista[0].append(num)
     else:
         lista[1].append(num)
     continuar= input("Continuar[S/N] : ")
     if continuar.lower().strip() == "s":
         continue
     elif continuar.lower().strip() == "n":
         print(f"Valores pares : {lista[0]}")
         print(f"Valores ímpares : {lista[1]}")
         break
     else:
         while continuar.lower().strip() != "s" and continuar.lower().strip() != "n":
             continuar = input("Continuar[S/N] : ")
         if continuar.lower().strip() == "s":
             continue
         elif continuar.lower().strip() == "n":
             print(f"Valores pares : {lista[0]}")
             print(f"Valores ímpares : {lista[1]}")
             break
         if continuar.lower().strip() == "n":
             break





