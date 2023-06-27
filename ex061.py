primeiro = int(input("Primeiro Termo : "))
último = int(input("Quantidade de termos : "))
razão = int(input("Razâo : "))
novo = 0
c = 0
print(f"Exibindo {último} termos da PA de {primeiro} com a razão {razão}",end=" = ")
while c < último:
  c = c + 1
  novo = primeiro + razão
  primeiro = novo
  print(novo, end=' , ' if c != último else ' -> ')
print("ACABOU!!!")