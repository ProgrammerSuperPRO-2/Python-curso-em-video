def jogadores(jogador ,gol=0 ):
    try:
     if jogador.isalpha():
         print(f"O jogador {jogador} ",end='')
     else:
         print(f"O jogador <desconhecido> ", end='')
    except:
        print(f"O jogador <desconhecido> ", end='')
def gols(gol):
    try:
        print(f"fez {gol} gols")
    except:
        print(f"fez 0 gols")



jogador = input("Jogador : ")

try:
   gol= int(input('Gols : '))
   jogadores(jogador)

   gols(gol)
except:
    jogadores(jogador)
    print(f"fez 0 gols")








