dinheiro = float(input("Dinheiro : R$"))
print('''[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] Em até 3x ou mais no cartão''')

escolha = int(input("Sua opção : "))

if escolha == 1:
    desconto = (10/100)*dinheiro
    dinheiro = dinheiro - desconto
    print(f"O seu pagamento à vista passará a valer {dinheiro} R$")
elif escolha == 2:
    desconto = (5/100)*dinheiro
    dinheiro = dinheiro - desconto
    print(f"O seu pagamento à vista passará a valer {dinheiro} R$")
elif escolha == 3:
    dinheiro2 = dinheiro /2
    print(f"Você deverá pagar duas parcelas de {dinheiro2} R$")
elif escolha == 4:
    desconto = (20/100)*dinheiro
    dinheiro2 = dinheiro + desconto
    parcelas = int(input("Parcelas : "))
    dinheirojuro = dinheiro2/parcelas

    print(f"Seu pagamento será parcelado em {parcelas}x de {dinheirojuro} e o valor final, com juros, será : {dinheiro2}")
