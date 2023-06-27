erros = 0
def leitura_num():
    global erros
    while True:
        number = str(input("Digite um número :"))
        if number.isnumeric():
            return number
        else:
            print("\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO...\033[m")
            erros = erros + 1



número = leitura_num()
contador = len(número)
print("~~~~~~~~~~~~~",end='')
print("~"*contador)
print(f"Você digitou {número}")
print("~~~~~~~~~~~~~",end='')
print("~"*contador)
print("Total de erros:",erros)