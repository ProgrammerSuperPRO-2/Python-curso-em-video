
def soma(valor=0,valor2=0):

 print(f"a soma entre {valor:.2f} e {valor2:.2f} é {valor + valor2:.2f} " )

try:
 valor = float(input("digite um valor: "))
 valor2 = float(input("digite outro valor: "))
except:
 print("Erro Enconrado")

soma(valor, valor2)