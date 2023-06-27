lista= 0
def notas(*args,sit =False):

    maior = args[0][0]
    menor = args[0][0]
    for elementos in args[0]:
        if elementos>maior:
            maior = elementos
    for elemento in args[0]:
        if elemento<menor:
            menor = elemento
    soma = 0
    for elem in args[0]:
        soma= elem+soma
        media = soma/len(args[0])
    if media >= 10:
        situação = 'PERFEITA'
    elif media>=9 and media <=9.9:
        situação = "INCRÍVEL"
    elif media > 8 and media < 9:
        situação = "ÓTIMA"
    elif media >7 and media<=8:
        situação = 'BOA'
    elif media > 6 and media <=7:
        situação = 'RAZOÁVEL'
    elif media > 5 and media <= 6:
        situação = "RUIM"
    elif media > 3 and media <= 5:
        situação = "MUITO RUIM"
    elif media > 1 and media <= 3:
        situação = "TERRÍVEL"
    elif media <= 1:
        situação = "A PIOR POSSÍVEL"

    if sit == False:
        kil = {'maior':maior,'menor':menor,'media':media}
    elif sit==True:
        kil = {'maior': maior, 'menor': menor, 'media': media,"situação":situação}
    return kil





c = 0
inputar = int(input("Quantidade de alunos na sua escola : "))
nota = []
for elementos in range(0,inputar):
    c = c+1
    notinha = float(input(f"Nota do aluno {c} : "))
    nota.append(notinha)
situação = input("Mostrar situação [S/N] : ")
while situação.strip().lower() != 's' and situação.strip().lower() != 'n':
    situação = input("Mostrar situação [S/N] : ")
if situação == 's':
    situação = True
else:
    situação = False


result = notas(nota,sit=situação)
print(result)