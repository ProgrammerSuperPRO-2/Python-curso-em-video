preço= float(input("preço do produto: "))
desconto = int(input("digite o desconto que esse produto receberá: "))
desconto_novo = (desconto/100)*preço
preço_novo = preço - desconto_novo
print(f"com um desconto de {desconto}%, esse produto de {preço}, passará a valer: {preço_novo:.2f}")
