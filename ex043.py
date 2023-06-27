from time import sleep
peso = float(input("peso (kg) : "))
altura = float(input("altura (m) : "))
imc = peso/(altura*altura)
print("\n\ncalculando imc...")
sleep(5)
print(f"\n\nseu IMC é : {imc} ")
sleep(5)
print("\ncom esse IMC, seu estado atual é : ")

if imc < 18.5:
    print("\33[1;33mMAGREZA")
if imc >= 18.5 and imc <= 24.9:
    print("\33[1;32mNORMAL")
if imc >= 25 and imc <= 29.9:
    print("\33[1;33mSOBREPESO")
if imc >= 30 and imc <= 34.9:
    print("\33[1;33mOBESIDADE GRAU 1")
if imc >= 35 and imc <= 39.9:
    print("\33[1;33mOBESIDADE GRAU 2")
if imc >= 40:
    print("\33[1;31mOBESIDADE MÓRBIDA, CUIDADO!")
