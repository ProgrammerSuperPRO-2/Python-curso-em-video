import random


def sorteio():
    lista = random.choice([1,2,3,4,5,6,7,8,9,10])
    lista1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    lista2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    lista3 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    lista4 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    total = [lista,lista1,lista2,lista3,lista4]
    return total
loos = sorteio()
def pares():
    par = []
    for elemento in loos:
        if elemento %2 ==0:
            par.append(elemento)
    return par
def soma_pares():
    soma = 0
    for elementos in pares():
        soma = soma + elementos
    return soma

print("Sorteando 5 valores da lista : ",loos)
print("Números pares : ",pares())
print("Soma de todos números pares : ",soma_pares())