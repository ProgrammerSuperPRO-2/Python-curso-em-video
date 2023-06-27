import datetime
def votos():
  data = datetime.date.today().year
  ano_nascimento = int(input("Ano de nascimento : "))
  idade = data - ano_nascimento
  if idade >= 18 and idade <= 70:
      print(f"Com {idade} anos : VOTO OBRIGATÓRIO")
  elif idade >= 16:
      print(f"Com {idade} anos : VOTO FACULTATIVO")
  elif idade<16:
      print(f"Com {idade} anos : VOTO NEGADO")

votos()
