Sexo = input("Sexo : ")

while True:
 if Sexo.upper() == "M" or Sexo.upper() == "F":
  print(f"Sexo {Sexo.upper()} registrado")
  break
 else:
  while Sexo != "M" and Sexo != "F":
    Sexo = input("Dados inválidos. Informe seu sexo : ").upper().strip()
