Lista_Num = []
Num_Pares = [""]
Num_Ímpares = [""]
Zero = False
while True:
    num = int(input("Número : "))
    Lista_Num.append(num)
    if num % 2 == 0:
        Num_Pares.append(num)
        if Num_Pares[0] == "":
            del Num_Pares[0]
    if num % 2 != 0:
        Num_Ímpares.append(num)
        if Num_Ímpares[0] == "":
            del Num_Ímpares[0]
    confirmação = input("continuar[S/N] : ")

    while confirmação.lower().strip() != "s" and confirmação.lower().strip() != "n":
        confirmação = input("continuar[S/N] : ")
    if confirmação.lower().strip() == "s":
        continue
    elif confirmação.lower().strip() == "n":
        break

if 0 in Num_Pares:
    neutro = input("Número zero é neutro [T/F] :")
    if neutro.lower().strip() == "t":
      print("Zero considerado neutro")
      Zero = False
      for c, elemento in enumerate(Num_Pares):
        if elemento == 0:
          del Num_Pares[c]
    elif neutro.lower().strip() == "f":
      print("Zero considerado par")
      Zero = True
    else:
      Zero = True
      print("Zero considerado par")



print("Lista Completa : ", Lista_Num)
if Num_Pares!= []:
 if Num_Pares[0] != "":
    print(f"Lista Dos Pares : ", Num_Pares)
 else:
    print("Lista Dos Pares : Sem Número Par")
else:
    print("Lista Dos Pares : Sem Número Par")


print("Lista Dos Ímpares : ", Num_Ímpares if Num_Ímpares[0] != "" else "Sem número ímpar")

if Zero == False:
    print("Número Neutro : [0]")




