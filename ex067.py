num = 0
fim = 0
while True:
 num = int(input("Multiplicador : "))
 if num < 0:
     print("PROGRAMA TABUADA ENCERRADO. Volte Sempre!")
     break
 fim = int(input("Multiplicando : "))
 for c in range (0,fim+1):
    tabuada = c * num
    print(f"{num} x {c:2} = ",tabuada)

