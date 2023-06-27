termo = int(input("primeiro termo : "))
razão = int(input("razão : "))

pa = termo + razão
print(termo,end=" -> ")

for c in range(0,9):
    pa = termo + razão
    print(pa, end=" -> " )
    termo = pa
print("ACABOU")