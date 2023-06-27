import time
def printer(palavra,arg):
    print(f"{arg}"*len(palavra))
    print(palavra)
    print(f"{arg}" * len(palavra))
while True:
    printer("SISTEMA DE AJUDA HELP",'\033[39;42m~')
    f = input("\033[mFunção ou biblioteca :").strip().lower()
    printer(f"ACESSANDO MANUAL DE COMANDO '{f}'",'\033[39;44m~')
    time.sleep(5)
    print('\033[30;47m')
    print(f'{help(f)} ')


