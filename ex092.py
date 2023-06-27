import datetime
hoje = datetime.date.today().year



nome = input("Nome : ").title()
while len(nome.split()) >= 2:
    print("nome não leva dois elementos")
    nome = input("Nome : ").title()
Nascimento = int(input("Ano de nascimento : "))

while Nascimento > hoje or Nascimento < hoje - 130:
    if Nascimento > hoje:
      print("Ano de nascimento maior que ano atual")
    elif Nascimento < hoje - 130:
      print("Ano de nascimento inválido")
    Nascimento = int(input("Ano de nascimento : "))




idade = hoje - Nascimento
ctps = int(input("Carteira de Trabalho [0 se não tem] : "))
dicionário = {'nome':nome,'idade':idade,'ctps':ctps}
if ctps > 0 :
    contratação = int(input("Ano de contratação : "))
    salário = float(input("Salário : "))
    aposentadoria = idade + 32
    dicionário['Adc'] = contratação
    dicionário['Salário'] = salário
    dicionário['aposentadoria'] = aposentadoria
    print("\n")
    print("-=-=" * 20)
    print("                                    DADOS")
    print("-=-="*20)
    print("Nome : ",dicionário["nome"])
    print("Idade : ", dicionário["idade"])
    print("Ctps : ", dicionário["ctps"])
    print("Ano de contratação : ", dicionário["Adc"])
    print("Salário : ", dicionário["Salário"])
    print("aposentadoria : ",dicionário['aposentadoria'])
else:
    print("\n")
    print("-=-=" * 20)
    print("                                    DADOS")
    print("-=-=" * 20)
    print("\nNome : ", dicionário["nome"])
    print("Idade : ", dicionário["idade"])
    print("Ctps : ", dicionário["ctps"])







