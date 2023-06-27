valores = []
while True:
    num = int(input("Digite um número : "))
    valores.append(num)
    mínimo = min(valores)
    máximo = max(valores)
    confirm=input("Continuar : ")
    if confirm.lower().strip() == "s":
        continue
    elif confirm.lower().strip() == "n":
        break
print(f"O maior valor é : {máximo}")
print(f"O menor valor é : {mínimo}")



