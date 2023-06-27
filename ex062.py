primeiro = int(input("Primeiro Termo da PA : "))
razão = int(input("Razâo da PA : "))
último = int(input("Quantidade de termos da PA : "))
print("\n",end="")
novo = 0
c = 1
print(f"PA",end=" : ")
print(primeiro,end=' , ')
while c < último:
  c = c + 1
  novo = primeiro + razão
  primeiro = novo
  print(novo, end=' , ' if c != último else ' -> ')
print("PAUSA!!!")


while c>=último:
  confirmação = input("\nVer mais [S/N] : ")
  print("\n",end="")
  if confirmação.lower().strip() == 's' or confirmação.lower().strip() == 'sim':
    for número in range(0,último):
     novo = primeiro + razão
     primeiro = novo
     print(novo, end=' , ' if c != último else ' -> ')
  else:
      break
  print("PAUSA")
print("SISTEMA ENCERRADO!!!")

