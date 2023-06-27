
nums = ("Zero","Um", "Dois", "Três","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze","Doze","Treze","Catorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove","Vinte")
n = 0
while True:
 if n <= 20:
  n = int(input("Número de 0 a 20 : "))
  if n> 20:
      while n>20:
          n = int(input("Número Inválido. Tente Um Número De 0 a 20 : "))


  for num in nums:
        recebe = nums[n]
  print(f"O número que você digitou foi {recebe}")








