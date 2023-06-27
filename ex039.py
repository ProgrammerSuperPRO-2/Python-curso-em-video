import datetime
Ano_Atual = datetime.date.today().year

Ano_Nascimento = int(input("Ano do seu nascimento: "))
idade = Ano_Atual - Ano_Nascimento
print(f"quem nasceu em {Ano_Nascimento} tem {idade} anos em {Ano_Atual}.")

if idade < 18 and idade != 18:
    futuro = 18 - idade
    print(f"ainda faltam {futuro} anos para o seu alistamento.")
    print(f"seu alistamento vai ser em {Ano_Atual+futuro}.")
if idade == 18:
    presente = 18
    print(f"seu alistamento deve ocorrer esse ano.")

elif idade > 18 and idade != 18:
    passado = idade - 18
    print(f"Você já deveria ter se alistado há {passado} anos")
    print(f"seu alistamento foi em {Ano_Atual - passado}.")

