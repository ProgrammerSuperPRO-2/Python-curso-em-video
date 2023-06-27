Lista_Operadores = ["-","+","*","/"]
print("Não aceitamos sinal de '='")
número = input("Digite sua expressão : ")

c = 0
f = 0

Sinais_inválidos = 0

lista = []
Algoritmo = False
for elementos in número:
 lista.append(elementos)

for elementos in lista:
    if elementos in Lista_Operadores:
        c = c + 1

if Lista_Operadores[0] in lista or Lista_Operadores[1] in lista or Lista_Operadores[2] in lista or Lista_Operadores[3] in lista:
          Algoritmo = True
else:
    Algoritmo = False
    print("\nERRO 1: Sem sinais de operação")
if lista[0] == Lista_Operadores[0] and lista[1].isnumeric() and c == 1:
    print("\nERRO 3.1: Isso é um número negativo, não uma expressão")
    p = 1
    Algoritmo = False
elif lista[0] == Lista_Operadores[1] and lista[1].isnumeric() and c == 1:
    p = 1
    print("\nERRO 3.2: Isso é um número positivo, não uma expressão")
    Algoritmo = False

else:
     if Lista_Operadores[0] in lista or Lista_Operadores[1] in lista or Lista_Operadores[3] in lista:
        if lista[0].isnumeric() or lista[0] == Lista_Operadores[0] and lista[1] not in Lista_Operadores or  lista[0]  ==  Lista_Operadores[1] and lista[1] not in Lista_Operadores or lista[0] ==  Lista_Operadores[2] and lista[1] not in Lista_Operadores or lista[0] ==  Lista_Operadores[3] and lista[1] not in Lista_Operadores:
                Algoritmo = True

     if lista[0] == Lista_Operadores[0] and lista[1].isnumeric() and c == 1 and p!=1:
         Algoritmo = False
         print("\nERRO 3.1: Isso é um número negativo, não uma expressão")

     if lista[0] == Lista_Operadores[1] and lista[1].isnumeric() and c == 1 and p !=1:
         print("\nERRO 3.2: Isso é um número positivo, não uma expressão")
         Algoritmo = False

     if lista[-1] in Lista_Operadores:
         print("\nERRO 4: Último termo é um sinal de operação")
         Algoritmo = False


if número.count("(") == número.count(")") and número.count("(")>0:
  for n, números in enumerate(lista):
   if "(" in números:
     if ")" in lista[n:]:
      if Lista_Operadores[0] in lista or Lista_Operadores[1] in lista or Lista_Operadores[2] in lista or Lista_Operadores[3] in lista:
        if lista[n+1].isnumeric():
            Algoritmo = True

else:
    if número.count("(")>número.count(")"):
     Algoritmo = False
     print("\nERRO 2.1: '(' em excesso ")
    elif número.count("(") < número.count(")"):
     Algoritmo = False
     print("\nERRO 2.2: ')' em excesso ")


for c, elementos in enumerate(lista):
    if lista[c] != "(" and lista[c] != ")":
        Sinais_inválidos = elementos.isnumeric()
        if elementos not in Lista_Operadores and Sinais_inválidos == False:
         f = f + 1

if f == 1:
    Algoritmo = False
    print("\nERRO 5: Termo inválido encontrado")
elif f > 1:
    Algoritmo = False
    print("\nERRO 5: Termos inválidos encontrados")

if "(" in lista and ")" in lista:
     if lista.index(")") < lista.index("("):
        print("\nERRO 6: Parênteses em posição errada")
        Algoritmo = False
if len(lista)>1:
 if lista[-1] == "(" or lista[-2] == "(":
    Algoritmo = False
if Algoritmo == True:
    print("\033[0;32m\nEXPRESSÃO CORRETA!!!\033[m")
else:
    print("\033[0;31m\nEXPRESSÃO ERRADA!!!\033[m")


