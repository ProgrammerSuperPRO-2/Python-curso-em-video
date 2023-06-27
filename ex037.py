número = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão: ")
print('''[ 1 ] Converter para OCTAL
[ 2 ] Converter para BINÁRIO
[ 3 ] converter para HEXADECIMA''')


escolha = int(input("Sua opção: "))

if escolha == 3:
    HEXADECIMAL = hex(número)
    HEXADECIMAL = str(HEXADECIMAL)
    HEXADECIMAL = HEXADECIMAL[2:]

    print(f"{número} convertido para HEXADECIMAL é igual a: ",HEXADECIMAL)

elif escolha == 2:
    BINÁRIO = bin(número)
    BINÁRIO = str(BINÁRIO)
    BINÁRIO = BINÁRIO[2:]

    print(f"{número} convertido para BINÁRIO é igual a: ",BINÁRIO)
elif escolha == 1:
    OCTAL = oct(número)
    OCTAL = str(OCTAL)
    OCTAL = OCTAL[2:]
    print(f"{número} convertido para OCTAL é igual a : ",OCTAL)
