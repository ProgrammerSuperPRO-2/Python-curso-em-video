maiores = 0
homens = 0
Mulheres_Menos_De_20 = 0
while True:
 print("------------------")
 print(" CADASTRE PESSOAS")
 print("------------------")
 idade = int(input("Idade : "))
 sexo = input("Sexo (M/F) : ")
 if sexo.lower().strip() == "m":
  homens = homens + 1
 confirm = input("Continuar [S/N] : ")
 if idade >= 18:
  maiores = maiores + 1
 if idade < 20 and sexo.lower().strip() == "f":
  Mulheres_Menos_De_20 = Mulheres_Menos_De_20+1
 if confirm.lower().strip() == "s":
  continue
 elif confirm.lower().strip() == "n":
  print("---------------------------------")
  print(f"Pessoas maiores de 18 : {maiores} ")
  print(f"Ao todo temos {homens} homens cadastrados ")
  print(f"Temos {Mulheres_Menos_De_20} mulheres com menos de 20 anos")
  print("---------------------------------")
  print("   PROGRAMA ENCERRADO!!!")
  break