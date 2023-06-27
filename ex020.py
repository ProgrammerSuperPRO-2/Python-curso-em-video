import random
aluno = []
cont = 0
print("bem vindo ao software de sorteio para os trabalhos em sala de aula")
while True:
    cont += 1
    aluno.append(input(f"aluno {cont}: "))
    if 'pare' in aluno:
        del aluno[-1]
        random.shuffle(aluno)
        print("a ordem de apresentação dos trabalhos será: ",aluno)
        break


