from math import sqrt
catetoB = float(input("Cateto oposto : "))
catetoC = float(input("Cateto adjecente : "))
hipotenusa = sqrt(catetoB**2 + catetoC**2)
print(f'com os catetos {catetoB:.2f} e {catetoC:.2f} identifica-se uma hipotenusa de valor : {hipotenusa:.2f}')