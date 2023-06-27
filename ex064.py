num = 0
dados = 0
c = 0
while num != 999:
    c = c + 1
    num = int(input("Digite um número [999]: "))
    if num == 999:
        break
    dados = dados + num
print(f"a soma dos {c} números é : ",dados)



