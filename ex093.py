soma = 0

dicionário = {'nome':input("Nome : "),'partidas':int(input("Partidas jogadas :")),'gols':[]}

for cada_gol in range(dicionário['partidas']):
     var = int(input(f"Gol na partida {len(dicionário['gols'])+1} : "))
     dicionário['gols'].append(var)
     soma = soma + var


for posição, cada_golaço in enumerate(dicionário['gols']):
     print(f"Na partida {posição+1}, fez {cada_golaço} gols")
print(f"Total de {soma} gols")