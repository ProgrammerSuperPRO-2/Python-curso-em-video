dias = int(input("dias com o carro : "))
km = float(input("kms rodados : "))
valor_dia = dias * 60
valor_km = 0.15*km
valor_total = valor_km + valor_dia
print(f"o valor que você precisa pagar pelo aluguel é de: {valor_total} R$")