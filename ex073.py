from operator import index

Colocados=('palmeiras','internacional','fluminence','corithians','flamengo',
'athletico PR','atletico MG','fortaleza','são paulo','botafogo','america','santos','goias',
'red bull bragantino','coritiba','cuiaba','ceara','atletico GO','avai','juventude')

print(f"Lista dos times do brasileirão : {Colocados}")
Primeiros = Colocados[0:5]
Últimos = Colocados[-1],Colocados[-2],Colocados[-3],Colocados[-4]
print(f"Os 5 melhores dessa temporada foram : {Primeiros}")
print(f"Os 4 piores dessa temporada foram : {Últimos}")
Coloc = sorted(Colocados)
print(f"Times em ordem alfabética : {Coloc}")

for n in range(0,len(Colocados)):
    if "palmeiras" in Colocados:
        print("palmeiras está na posição",Colocados.index("palmeiras")+1)
        break


