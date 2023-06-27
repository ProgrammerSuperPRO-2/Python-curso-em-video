num = []
contador = 0
while True:
    contador = contador + 1
    num.append(int(input(f'Digite o {contador}º valor : ')))
    continuar = input('Continuar[S/N] : ')
    if continuar.lower().strip() == 'n':
        break
    elif continuar.lower().strip() == 's':
        continue
    else:
        while continuar.lower().strip() != 's' and continuar.lower().strip() != 'n':
            continuar = input('continuar[S/N] : ')
num.sort(reverse=True)
if len(num) > 1:
    print(f"Essa lista tem {len(num)} números")
if len(num) == 1:
    print(f"Essa lista tem {len(num)} número")

print("Os números em ordem decrescente são : ", num)
if 5 in num:
    print("O valor cinco faz parte da lista")
else:
    print("O valor cinco não faz parte da lista")
