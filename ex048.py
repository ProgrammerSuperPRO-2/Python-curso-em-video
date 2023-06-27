count = 0
c2 = 0

for c in range(0, 500):

    if c % 2 != 0:
        if c % 3 == 0:
            count = count + 1
            v = c2 + c
            c2 = v
print(f"a soma de todos os {count} valores solicitados é de : {c2}")


