Valor_Total = 0
Preço_Caro = 0
Produto_Barato = 0
Maio = 0
Menor = 0
p = 0
cont = 0
while True:
    cont = cont+1
    print("--------------------------")
    print("  LOJA SUPER BARATÃO")
    print("--------------------------")
    nome = input("Nome Do Produto : ")
    preços = int(input("Preço Do Produto R$"))
    if cont == 1:
        Produto_Barato = nome
        Menor = preços
    if preços > 1000:
        Preço_Caro +=1
    Valor_Total= Valor_Total + preços
    Maior = preços
    if Maior > p:
        Maior = preços

    else:
        Menor = preços
        Produto_Barato = nome
    p = preços
    confirm = input("Continuar [S/N] : ")
    if confirm.strip().lower() == "s":
        continue
    if confirm.strip().lower() == "n":
        print("\033[0;33m-------------------------------------------------------")
        print("              Finalização Das Compras")
        print("-------------------------------------------------------")
        print(f"O total da compra foi R${Valor_Total}.00")
        print(f"temos {Preço_Caro} produtos custando mais de R$1000.00")
        print(f"O produto mais barato foi {Produto_Barato}, custando R${Menor}.00")
        print("\033[0;31m-------------------------------------------------------")
        print("                   LOJA FECHADA!!!")
        print("-------------------------------------------------------")
        break









