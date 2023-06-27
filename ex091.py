from random import randint
import time


print("Valores sorteados : ")
lista = {'jogador1': randint(0,6),'jogador2':randint(0,6),'jogador3':randint(0,6),'jogador4':randint(0,6)}
for c, elementos in lista.items():
    print(f'{c} tirou {elementos}')
print("===============================================RANKING DOS JOGADORES==================================================")
lis=  sorted(lista.items(),reverse = True)
for item in sorted(lista, key = lista.get):
    n = lista[item]
co= 0
for c, elemento in enumerate(lista):
    time.sleep(2)
    co = co+1
    print(f"{co}ºlugar = ",lis[c][0],f" , com o número {lis[c][1]}")





