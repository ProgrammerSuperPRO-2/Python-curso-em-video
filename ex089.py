lista_notas = []
lista_nomes = []
lista_media = []
c = 0
nota1 = 9999999999
nota2 = 9999999999


def média_de_vários_alunos():
    while True:
        nome = input("nome do aluno : ")
        lista_nomes.append(nome)
        nota1 = int(input("Nota 1 :"))
        while nota1 > 10:
            print("nota maior que 10, repita.")
            nota1 = int(input("Nota 1 :"))

        nota2 = int(input("Nota 2 :"))
        while nota2 > 10:
            print("nota maior que 10, repita.")
            nota2 = int(input("Nota 2 :"))

        if nota1 <= 10 and nota2 <= 10:
            lista_notas.append([nota1, nota2])
            media = (nota1 + nota2) / 2
            lista_media.append(media)
            continuar = input("Continuar [S/N] : ").strip().lower()
            if continuar == "s":
                continue
            elif continuar == "n":
                break
            else:
                while continuar != "s" and continuar != "n":
                    continuar = input("Continuar [S/N] : ").strip().lower()
                if continuar == "s":
                    continue
                elif continuar == "n":
                    break

    def lista():
        print("\nNº", end=' ')
        print(" aluno", end=' ')
        print("             média")
        print("------------------------------------------")

        for c, elemento in enumerate(lista_nomes):
            print(f"{c}   {elemento:<20}{lista_media[c]}")
        print("------------------------------------------")

    lista()

    while True:
        try:

            pedir = input(
                "\nNotas do aluno desejado ('parar' para interromper) ('exibir' para exibir tabela) : ").strip().lower()
            if pedir.strip().lower() == "parar":
                break
            elif pedir.strip().lower() == 'exibir':
                lista()

            else:
                print(f"\nnotas do aluno {lista_nomes[pedir]} é : {lista_notas[pedir]}")
                print("------------------------------------------")
        except:
            print("\naluno não identificado")
            print("------------------------------------------")


if __name__ == "__main__":
    média_de_vários_alunos()
