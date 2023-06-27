import random

Ímpar = 0
Par = 1
result = 0
Tentativas = 0
while True:
    Num = int(input("Número : "))
    Escolha = input("Ímpar ou Par [I/P] :")
    Computador = random.randint(0, 10)

    soma = Computador + Num

    if soma%2 != 0:
        result = 1
    elif soma%2 == 0:
        result = 0
    if Escolha.upper().strip() == "I" and result == 0:
        print(f"\nVocê jogou {Num} e o computador {Computador}. Total de {soma} DEU PAR")
        print(f"GAME OVER! Você ganhou {Tentativas} vezes nessa rodada")
        break
    elif Escolha.upper().strip() == "P" and result == 0:
        print(f"\nVocê jogou {Num} e o computador {Computador}. Total de {soma} DEU PAR")
        print("Você Venceu! Vamos Jogar Novamente...\n")
        Tentativas = Tentativas+1
        continue
    elif Escolha.upper().strip() == "P" and result == 1:
        print(f"\nVocê jogou {Num} e o computador {Computador}. Total de {soma} DEU ÍMPAR")
        print(f"GAME OVER! Você ganhou {Tentativas} vezes nessa rodada")
        break
    elif Escolha.upper().strip() == "I" and result == 1:
        print(f"\nVocê jogou {Num} e o computador {Computador}. Total de {soma} DEU ÍMPAR")
        print(f"Você Venceu! Vamos Jogar Novamente...\n")
        Tentativas = Tentativas + 1
        continue







vezesvezesvezesvezesvezesvezesvezesvezesvezesvezesvezesvezesvezesvezesvezesvezesvezesvezesvezes
