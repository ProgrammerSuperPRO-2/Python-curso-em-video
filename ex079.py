Valores = []
Repetidos = []
while True:
    Entrada = int(input("Digite um valor : "))
    if Entrada in Repetidos:
        print("Valor repetido, não iremos adicioná-lo à lista!")
    else:
        print("Valor adicionado com sucesso!")
        Valores.append(Entrada)

    Repetidos.append(Entrada)
    confirmação = input("Continuar [S/N] : ")

    while confirmação.lower().strip() != "s" and confirmação.lower().strip() != "n":
        confirmação = input("Continuar [S/N] : ")

    if confirmação.lower().strip() == "s":
        continue
    if confirmação.lower().strip() == "n":
        Valores.sort()
        print("Os valores da sua lista (em ordem crescente) são : ", Valores)
        break
