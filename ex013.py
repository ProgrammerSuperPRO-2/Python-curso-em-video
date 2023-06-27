salário= float(input("salário: "))
aumento = int(input("porcentagem do aumento salarial: "))
salário_novo = (aumento/100)*salário
aumento_novo = salário + salário_novo
print(f" esse funcionário que ganhava {salário}, passará a ganhar: {aumento_novo:.2f}")