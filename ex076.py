lista = ["Açucar", 2,"Pera",4,"Uva",3,"Abacate",5]
print('----------------------------------------')
print("LISTAGEM DE PREÇOS")
print('----------------------------------------')
for itens in range(0,len(lista)):
    if itens %2 == 0:
        print(f"{lista[itens]:.<30}",end=" ")
    else:
        print(f"{lista[itens]}R$")