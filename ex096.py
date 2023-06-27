print("Controle de terrenos")
print("---------------------------------------------------------")
largura = float(input("LARGURA : "))
comprimento = float(input("COMPRIMENTO : "))
def área():
    area = largura * comprimento
    return area

print(f"Área de um terreno {largura}x{comprimento} é : ",área())