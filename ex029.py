pergunta = int(input("Velocidade atual do carro em km/h : "))
if pergunta > 80:
    limite = pergunta - 80
    multa = limite * 7

    print(f"\33[1;31mMULTADO!!! VOCÊ ULTRAPASSOU O LIMITE DE 80km/h.\nSua multa será de \33[1;33m{multa}\33[M R$\33[m")
    print("\33[1;32mTenha um bom dia! Dirija com segurança.\33[m")

else:
    print("\33[1;32mTenha um bom dia! Dirija com segurança.\33[m")
