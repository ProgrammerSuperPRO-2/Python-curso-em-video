import time
soma = 0
lista = []
while True:
    dicionário = {'nome':input("Nome : "),'partidas':int(input("Partidas jogadas :")),'gols':[]}
    for cada_gol in range(dicionário['partidas']):
         var = int(input(f"    Gol na partida {len(dicionário['gols'])+1} : "))
         dicionário['gols'].append(var)

    lista.append(dicionário)
    continuar = input("Continuar [S/N] : ")
    while continuar.strip().lower() != 's' and continuar.strip().lower() != 'n':
        continuar = input("Continuar [S/N] : ")
    if continuar.strip().lower() == 'n':
        break
print("-=-=-"*120)
print("cod",end='')
print("  nome                    ",end='')
print("partidas                    ",end='')
print("gols por partida")
print("-----"*120)
for elementos in range (0,len(lista)):
    nomi = lista[elementos]['nome']
    gola = lista[elementos]['partidas']
    print(f'  {elementos:<2}',f"{nomi:<27}",end='')
    print(f"{gola:<25}",end='')
    print(f"{lista[elementos]['gols']}")

print("-----"*120)
jogador = 0
soma = 0
while jogador !=999:
    jogador = int(input("Escolher jogador para avaliar : "))

    if jogador > len(lista):
        print("Sem jogador com esse índice")
    print("-----"*120)
    posição = jogador
    print("---LEVANTAMENTO DO JOGADOR",lista[jogador]['nome'],":")
    for posição, cada_golaço in enumerate(lista[posição]['gols']):
        print(f"Na partida {posição+1}, fez {cada_golaço} gols")
        soma = cada_golaço + soma
    print("-----" * 120)
    print(f"Total de {soma} gols")
    continuar = 0
    continuar = input("\nContinuar [S/N] : ")
    while continuar.strip().lower() != 's' and continuar.strip().lower() != 'n':
        continuar = input("Continuar [S/N] : ")
    if continuar.strip().lower() == 'n':
        break
    print("")
    print("")
    print("")
    print("=-=-"*120)
    print("cod", end='')
    print("  nome                    ", end='')
    print("partidas                    ", end='')
    print("gols por partida")
    print("-----" * 120)


    for elementos in range(0, len(lista)):
        nomi = lista[elementos]['nome']
        gola = lista[elementos]['partidas']
        print(f'  {elementos:<2}', f"{nomi:<27}", end='')
        print(f"{gola:<25}", end='')
        print(f"{lista[elementos]['gols']}")
    print("-----" * 120)
