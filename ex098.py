import time
print("-=-="*20)
print("Contagem de 1 a 10 : ")
tempo = 12
d = 0

for ci in range(1,11):
    time.sleep(1)
  
    print(ci,end=' ')
print("")
print("-=-=" * 20)
print("Contagem de 10 a 0 pulando de 2 em 2 : ")

while tempo>1:
    tempo = tempo - 2
    time.sleep(1)
    print(tempo, end=' ')

print("")
print("-=-="*20)
print("Agora é a sua vez de personalizar a contagem")
a = int(input("Início : "))
b = int(input("Fim : "))
p = int(input('passo : '))
if p<0:
 pi = str(p)
 print(f"Contagem de {a} até {b} em {pi[1:]}")
else:
 print(f"Contagem de {a} até {b} em {p}")
if '-' in str(p):
    p = str(p)
    p = p[1:]
    p = int(p)
if a<b:
    for ele in range(a,b,p):
        time.sleep(1)
        print(ele, end=' ')

else:
    while b<a:

        print(a,end=' ')

        time.sleep(1)
        a = a - p




print("")
print("-=-="*20)