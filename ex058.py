import random
from time import sleep
from colorama import Fore, Back, Style
import sys

frase = 'BEM VINDO AO PROGRAMA DE ADVINHAÇÃO'


print(f' \033[0;30;43m{frase:^70}\033[m')


decot = '='
print(f'{71*decot}')
sleep(5)

print('eu pensei em um número de 1 a 100')

sleep(2)



'''n= [1,2,3,4,5,6,7,8,9,10,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]

n=random.choice(n)'''

n=random.randint(1,100)
n2= random.randint(1,3)
r= 0
count= 0
sorte = random.randint(1,100)
sorte2= n+n2
sorte3= random.randint(1,100)
g= random.randint(1,10)
g2= random.randint(-10,-1)



while r != n:

     r= int(input('\nem qual número eu pensei? '))
     count= count+1

     if r == sorte2:
         print(f' \nDICA: O VALOR ESTÁ BEM PRÓXIMO DE {sorte2}')

     if n> 10 and r == sorte3: print(f' o valor está entre {n-g} e  {n+g} ')



     if r == sorte and n%2 == 0 and n!= sorte: print('\nDICA: O NÚMERO É PAR')
     elif r == sorte and n%2>0 and n!=sorte :print('DICA: O NÚMERO É ÍMPAR')
     elif n == sorte:
         sorte = sorte + 1
     elif r > n and r<=100:
         print(f'\n\033[0;36m\nO número em que eu pensei é menor que {r}\033[m')


     elif r < n and r>0 : print(f'\n\033[0;33mO número em que eu pensei é maior que {r}\033[m')


     elif r> 100: print("\n\033[0;31messe número não é válido\033[m")
     elif r<=0:print('\n\033[0;31messe número não é válido\033[m')
     if count== 5:
        print("\nVocê já errou 5 vezes")
     if count == 10:
        print("\nVocê já errou 10 vezes")
     if count== 20:
        print("\nVocê já errou 20 vezes")
     elif r> 100: print("\n\033[0;31messe número não é válido\033[m")
     elif r<=0:print('\n\033[0;31messe número não é válido\033[m')


     elif r == n and 5 < count< 10 : print(Fore.GREEN+ f'\nPARABÉNS! VOCÊ ACERTOU O NÚMERO EM APENAS {count} TENTATIVAS') and sys.exit()

     elif r == n and count == 10: print(Fore.GREEN+'VOCÊ ACERTOU O NÚMERO, MAS FORAM NECESSÁRIAS 10 TENTATIVAS. \n TENTE FAZER MELHOR NA PRÓXIMA') and sys.exit()

     elif r == n and 10 < count <=20: print(Fore.GREEN+ f'você acertou, mas precisou de {count} tentativas; um baixo desempenho') and sys.exit()

     elif r== n and count >20: print(Fore.GREEN+f'você precisou de {count} tentativas para acertar esse número, Por acaso estava só chutando? Isso não é normal') and sys.exit()

     elif r== n and count <=5: print(Fore.GREEN + f'INCRÍVEL, VOCÊ ACERTOU EM {count} TENTATIVAS. ESSE RESULTADO É ESPETACULAR')

     if r == 111:sys.exit()
