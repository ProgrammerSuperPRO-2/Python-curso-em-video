import random
import time
import sys
alunos = []
f = ''
cont = 0
while True:
    f = ''
    cont += 1
    alunos.append(input(f"\nqual o nome do aluno {cont}:  "))
    continuar= input("quer continuar?").lower().strip()

    while True:
     if continuar.lower().strip() == 'sim' or continuar.lower().strip() == 'não':
         if continuar == 'sim':
             break
         elif continuar.lower().strip() == 'não':
             print(f"\ndentre os alunos : {alunos}, o sorteado foi...")
             time.sleep(5)
             escolhido = random.choice(alunos)
             print(f"\n\033[31m {escolhido.upper()} \033[m")
             sys.exit()

     else:
         print("não te entendemos")
         continuar = input("\n quer continuar?").lower().strip()







