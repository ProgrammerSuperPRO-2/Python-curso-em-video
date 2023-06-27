idades = []
nomes_mulheres = []
nomes = []
sexos = []
maior_que_media = []
while True:
    nome = input("Nome : ")

    nomes.append(nome)
    idade = int(input("Idade : "))

    idades.append(idade)
    sexo =input("Sexo[M/F] : ")
    while sexo.strip().lower() != 'm' and sexo.strip().lower() != 'f':
        sexo = input("Sexo[M/F] : ")
    if sexo.strip().lower() == "f":

        nomes_mulheres.append(nome)

    sexos.append(sexo)
    continuar = input("Continuar [S/N]  : ")
    while continuar.strip().lower() != 's' and continuar.strip().lower() != 'n':
           continuar = input("continuar [S/N] : ")
    if  continuar == "s":
        print("-----------------------------------------------------")
        continue

    if continuar == 'n':
        break
soma = 0
quant_nomes = len(nomes)
print(f"A) ao todo temos {quant_nomes} pessoas cadastradas")
print(f"B) mulheres cadastradas : {nomes_mulheres} ")
for posição, elementos in enumerate(idades):
    soma = idades[posição] + soma
media_idade = soma/quant_nomes
print("C) Media de idade : ",media_idade)


print("D) Pessoas com idade maior que a média : ")
for cia, elementos in enumerate(idades):
    if elementos > media_idade:
       maior_que_media.append(elementos)
       print("         nome : ",nomes[cia],end=';')
       print(" sexo : ", sexos[cia].upper(),end=';')
       print(" idade : ", idades[cia],end=';')








