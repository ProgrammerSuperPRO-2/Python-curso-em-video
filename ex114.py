from urllib import request
while True:
    try:
        site = input("Coloque a URL do site : ")
        if site.strip().lower() == 'finalizar':
            break
        else:
            t = request.urlopen(site)
            print("Site acessível")
    except:
        print("Site inacessível")
    continuar = input("\nCONTINUAR [S/N] : ").strip().lower()
    while continuar != 's' and continuar != 'n':
        continuar = input("\nCONTINUAR [S/N] : ").strip().lower()
    if continuar == 's':
        continue
    else:
        break
