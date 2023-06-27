lista = []
for c in range(0,5):
    num = int(input("Digite o valor : "))
    if c == 0 or num>lista[-1]:
        lista.append(num)
        print("Valor adicionado na última posição")
    else:
        pos = 0
        while pos<len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print("Valor adicionado na posição", pos+1)
                break
            pos = pos + 1

print(lista)









