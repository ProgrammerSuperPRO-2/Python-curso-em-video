erro = True
while erro:
    try:
        inteiro = int(input("Digite um número INTEIRO : "))
        erro = False
    except:
        print("\033[31mERRO!Isso não é um número inteiro...\033[m")
erro = True
while erro:
    try:
        inteiro = float(input("Digite um número REAL: "))
        erro = False
    except:
        print("\033[31mERRO!Isso não é um número real...\033[m")



