'''casa = float(input("Valor da casa : "))
salário = float(input("salário do comprador : "))
financiamento = int(input("Anos de financiamento : "))

p = casa/(financiamento*12)

if (30/100) * salário > p:
    print(f"Para pagar uma casa de {casa} R$ em {financiamento} anos, a prestação será de {p:.2f} R$")
    print("EMPRÉSTIMO pode ser CONCEDIDO!")
else:
    print(f"Para pagar uma casa de {casa} R$ em {financiamento} anos, a prestação será de {p:.2f} R$")
    print("Empréstimo NEGADO!")'''

casa = float(input('Digite o valor da casa: '))
salario = float(input('Diigite o salário do comprador: '))
anos = int(input('Em quantos anos irá pagar? '))
parcela = casa / (anos*12)
print(parcela)
if parcela > salario + (salario * 30 / 100):
      print('A compra foi negada.')
elif salario >= parcela:
      print('Parabéns! Você conseguiu!')

