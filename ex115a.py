from sys import exit as ex

opção = 0

def Menu_Principal(Texto_Exibir):
    print("--"*20)
    print(Texto_Exibir.center(40))
    print("--" * 20)
    print("\033[33m1 -\033[34m Ver pessoas cadastradas ")
    print("\033[33m2 -\033[34m Cadastrar nova Pessoa ")
    print("\033[33m3 -\033[34m Sair do Sistema\033[m ")
    print("--" * 20)
def pedir_opção():
    while True:
     global opção
     try:
        opção = int(input("\033[33mSua opção:\033[m"))

        if opção>3 or opção <=0:
            print(f"\033[31mOpção {opção} não existe\033[m")
            while True:
                opção = int(input("\033[33mSua opção:\033[m"))
                if opção > 3:
                    print(f"\033[31mOpção {opção} não existe\033[m")
                else:
                    break
        else:
            break

     except TypeError:
         print(f"\033[31mErro do tipo {TypeError} ")
     except ValueError:
        print(f"\033[31mErro do tipo {ValueError}")
     except NameError:
         print(f"\033[31mErro do tipo {NameError}")
def exibir_opções():
    if opção == 1:
        print("--"*20)
        print("Opção 1".center(40))
        print("--" * 20)
    if opção == 2:
        print("--"*20)
        print("Opção 2".center(40))
        print("--" * 20)
    if opção == 3:
        print("--"*20)
        print("     Saindo do Sistema... Até logo!".center(40))
        print("--" * 20)
        ex()



while True:
    pedir_opção()
    exibir_opções()










