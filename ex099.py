import random
import time

print("=-=-" * 30)
def maximo(a):
    print("Analisando valores passados...")
    for elementos in a:
     print(elementos,end=' ')
     time.sleep(0.5)
    print(f"...Foram informados {len(a)} valores ao todo...")

    try:
        tamanho = max(a)
        print("O maior valor informado foi", tamanho)
        print("=-=-" * 30)
    except:
        print("...Lista7 possui erro...")
        print("=-=-" * 30)





lista = [0,1,2,3,4,5,6]
lista1 = [0,1,4,3,8,10,4]
lista3 = [0,1,4]
lista4 = [0,1]
lista5 = [0]
lista6 = [1,2,3,4,5,6,56]
lista_erro = []

maximo(lista)
maximo(lista1)
maximo(lista3)
maximo(lista4)
maximo(lista5)
maximo(lista6)
maximo(lista_erro)






