maior = 0
menor = 0
valores = int(input("Digite um valor : ")),int(input("Digite um valor : ")),int(input("Digite um valor : ")),int(input("Digite um valor : "))
maior = valores[0]
menor = valores[0]
for valor in valores:
    if valor > maior:
        maior = valor
    if valor<menor:
        menor = valor
print(f"Valor {maior} é o maior  número e está na posição", end=' ')

for posição, número in enumerate(valores):
    if número == maior:
        print(f"{posição+1}...",end=' ')

print(f"\nValor {menor} é o menor  número e está na posição", end=' ')
for posição, número in enumerate(valores):
    if número == menor:
        print(f"{posição+1}...", end=' ')

