salario = float(input("digite seu salário : "))

salario15a = (15/100) * salario
salario15b = salario + salario15a

salario10a = (10/100) * salario
salario10b = salario + salario10a

if salario <= 1250:
    print(f"Quem ganhava {salario} R$ ,com aumento de 15%, passa a ganhar : {salario15b} R$")

if salario > 1250:
    print(f"Quem ganhava {salario} R$ ,com aumento de 10%, passa a ganhar : {salario10b} R$")

