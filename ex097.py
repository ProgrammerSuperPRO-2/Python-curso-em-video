def printer(palavra):
    print("~"*len(palavra))
    print(palavra)
    print("~" * len(palavra))
while True:
    Frase = input("Digite sua frase : ")
    printer(Frase)
