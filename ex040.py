nota1 = float(input("\33[1;37mPrimeira nota do aluno: "))
nota2 = float(input("Segunda nota do aluno: "))
media = (nota1 + nota2) / 2

if media > 5 and media <= 6.9:
    print(f"tirando {nota1} e {nota2}, a média do aluno é {media}")
    print("O aluno está de RECUPERAÇÃO")
elif media <= 5:
    print(f"tirando {nota1} e {nota2}, a média do aluno é {media}")
    print("O aluno está REPROVADO")
elif media > 7:
    print(f"tirando {nota1} e {nota2}, a média do aluno é {media}")
    print("O aluno está APROVADO")