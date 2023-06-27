def fat(f,show =0):
    fi = f
    lista = [f]
    j = f+1
    if show==True:
        for elemento in range(1,f+1):
            j = j-1
            print(j,end='X' if elemento < f else ' = ')
    elif show == False:
        pass
    for c in range(0,f):
     while f>1:
         fi = fi - 1
         result = lista[-1] *fi
         lista.append(result)
         f = f-1
    sus = str(result)
    if len(sus) > 10:
        print(f"{sus[0]}.{sus[1:4]}x10^{len(sus[1:])}")
    else:
        print(result)


fatorial = int(input("Fatorial : "))
mostrar = input("Mostrar multiplicadores [F/T] :").strip().lower()
while mostrar != 'false' and mostrar != 'true' and mostrar != 'f' and mostrar != 't':
    print('Resposta inválida, escolha entre TRUE ou FALSE')
    mostrar = input("Mostrar multiplicadores [F/T] :").strip().lower()

if mostrar == 'f' or mostrar == 'false' :
        mostrar = False
elif mostrar == 't' or mostrar == 'true':
        mostrar = True

fat(fatorial,show = mostrar)
