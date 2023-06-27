nome_geral = []
maior = 0
menor = 0
listas_pesos = []
novo_nome_menor = []
novo_nome_maior = []
while True:
   lista_nomes = input("Nome : ")
   lista_peso = float(input("peso : "))
   listas_pesos.append(lista_peso)
   string_peso = str(lista_peso)
   nome_geral.append(lista_nomes)
   if menor > lista_peso:
     menor = lista_peso
     novo_nome_menor.append(lista_nomes)
     if string_peso in novo_nome_menor:
       novo_nome_menor.append(lista_nomes)
   elif maior < lista_peso:
     maior = lista_peso
     novo_nome_maior.append(lista_nomes)
     if string_peso in novo_nome_maior:
       novo_nome_maior.append(lista_nomes)
   continuar = input("Continuar[S/N] : ")
   if continuar.lower().strip() == "s":
       continue
   elif continuar.lower().strip() == "n":
       break
   else:
       while continuar.lower().strip() != "s" and continuar.lower().strip() != "n":
           continuar = input("Continuar[S/N] : ")
           if continuar.lower().strip() == "s":
               continue
           elif continuar.lower().strip() == "n":
               break
       if continuar.lower().strip() == "n":
               break

if max(listas_pesos) == min(listas_pesos):
    print(f"{nome_geral} possuem os mesmos pesos")
else:
    if len(novo_nome_maior) > 1:
     print(f"{novo_nome_maior} possuem os maiores pesos de : {max(listas_pesos)}kg")
    else:
     print(f"{novo_nome_maior} possue o maior peso de : {max(listas_pesos)}kg")

    if len(novo_nome_menor) > 1:
     print(f"{novo_nome_maior} possuem os maiores pesos de : {max(listas_pesos)}kg")
    else:
     print(f"{novo_nome_menor} possue o menor peso de : {min(listas_pesos)}kg")
