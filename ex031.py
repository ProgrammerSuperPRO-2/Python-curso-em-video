pergunta = float(input("distância da viagem : "))
if pergunta < 200:
    valor = pergunta * 0.5
    print(f"a sua viagem irá lhe custar {valor}")
else:
    valor = pergunta * 0.45
    print(f"a sua viagem, com desconto, irá lhe custar {valor}")