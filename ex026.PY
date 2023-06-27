frase = input("frase desejada : ").lower().strip()
print(f"A frase tem {frase.count('a')} letras A;")
print(f"A primeira letra A aparece em: {frase.find('a')};")
print(f"A última letra A aparece em: {frase.rfind('a')}.")