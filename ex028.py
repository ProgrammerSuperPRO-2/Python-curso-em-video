import random
from time import sleep
def boas_vindas():
 print('\33[1;33m=-=\33[m'*23)
 print('\33[1;34mVOU PENSAR EM UM NÚMERO DE 0 ATÉ 5; TENTE ADVINHAR O QUE EU PENSEI...\33[m' )
 print('\33[1;33m=-=\33[m' * 23)
boas_vindas()

numero = random.randint(0,5)
pergunta = int(input("número em que eu pensei : "))
print('\33[1;35mPROCESSANDO...\33[m')
sleep(5)

if pergunta == numero:
    print('\33[1;33mVocê acertou. Parabéns\33[m')
else:
    print(f'\33[1;31mVocê errou. O número em que eu pensei foi {numero}\33[m')



