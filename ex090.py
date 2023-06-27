nome = input("nome do aluno : ")
media = int(input("média do aluno : "))
if media >= 5:
    aprovado = True
else:
    aprovado =False


aluno = {'nome':nome,"media":media,"situação":aprovado if aprovado == True else print("ol")}
print(f"nome é igual a {aluno['nome']}")
print(f"media é igual a {aluno['media']}")
if aprovado:
    print("situação do aluno : aprovado(a)")
else:
    print("situação do aluno : reprovado(a)")