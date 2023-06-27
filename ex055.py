peso = float(input("Peso : "))
menor = peso
maior = peso
for pesos in range(0, 5):
    peso = float(input("Peso : "))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f"O maior peso lido foi de : {maior} ")
print(f"O menor peso lido foi de : {menor}")
