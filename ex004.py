def avaliação():
    frase = input("digite alguma frase ou palavra: ").split()
    fras= ''.join(frase)

    print("\no tipo primitivo dessa frase é:",type(fras),"\n")

    if fras.isnumeric():
        print("essa frase possui apenas números")
    elif fras.isalpha():
        print("essa frase possui apenas letras")
    elif fras.isalnum():
        print("essa frase possui apenas letras e números")

    if fras.islower():
        print("essa frase  possui apenas letras minúsculas")
    elif fras.isupper():
        print("essa frase possui apenas letras maiúsculas")
    if fras.isspace():
        print("a frase só tem espaço")
    if fras.isdecimal():
        print("a frase tem decimais")
    if "a" in fras.lower():
        f = fras[:].lower()
        fa = f.count("a")
        if fa != 1:
         print(f"\nessa frase possui {fa} letras 'A'")
        elif fa == 1:
         print(f"\nessa frase possui 1 letra 'A'")
    if "e" in fras.lower():
        f = fras[:].lower()
        fa = f.count("e")
        if fa != 1:
         print(f"essa frase possui {fa} letras 'E'")
        elif fa == 1:
         print(f"essa frase possui 1 letra 'E'")
    if "i" in fras.lower():
        f = fras[:].lower()
        fa = f.count("i")
        if fa != 1:
            print(f"essa frase possui {fa} letras 'I'")
        elif fa == 1:
            print(f"essa frase possui 1 letra 'I'")
    if "o" in fras.lower():
        f = fras[:].lower()
        fa = f.count("o")
        if fa != 1:
            print(f"essa frase possui {fa} letras 'O'")
        elif fa == 1:
            print(f"essa frase possui 1 letra 'O'")
    if "u" in fras.lower():
        f = fras[:].lower()
        fa = f.count("u")
        if fa != 1:
            print(f"essa frase possui {fa} letras 'U'")
        elif fa == 1:
            print(f"essa frase possui 1 letra 'U'")
avaliação()