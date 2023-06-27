def nomes():
    c = []
    while True:
        try:

            nome = input("digite seu PRIMEIRO nome: ").strip().split()
            nome2 = input("digite seu SEGUNDO nome: ").strip().split()
            nam = ''.join(nome)
            nam2 = ''.join(nome2)
            nam_complet= (nam,nam2)
            c.append(' '.join(nam_complet))
            print(f'{nam.capitalize()} {nam2.capitalize()} seja bem vindo ao site! ')
            continuar = input("quer continuar? ")
            if continuar == "não":
                print(c)
                break
        except:
            print("ocorreu um erro")
'''if __name__ == "__main__":
    nomes()'''















