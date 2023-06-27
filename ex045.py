import random
import time

escolha = ["tesoura", "papel", "pedra"]
escolha = random.choice(escolha)
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
try:
 jogador = int(input("Sua opção : "))
 time.sleep(0.3)
 print("JO")
 time.sleep(0.5)
 print("KEN")
 time.sleep(0.5)
 print("PÔ")
 time.sleep(0.5)
 print("-="*20)

 if escolha == "pedra" and jogador == 0:
    print(f"Computador jogou {escolha.upper()}")
    print(f"Jogador jogou PEDRA")
    print("Empate")
 elif escolha == "papel" and jogador == 1:
    print(f"Computador jogou {escolha.upper()}")
    print(f"Jogador jogou PAPEL")
    print("Empate")
 elif escolha == "tesoura" and jogador == 2:
    print(f"Computador jogou {escolha.upper()}")
    print(f"Jogador jogou TESOURA")
    print("Empate")
 elif escolha == "pedra" and jogador == 1:
    print(f"Computador jogou {escolha.upper()}")
    print(f"Jogador jogou PAPEL")
    print("Jogador ganhou")
 elif escolha == "pedra" and jogador == 2:
    print(f"Computador jogou {escolha.upper()}")
    print(f"Jogador jogou TESOURA")
    print("Computador ganhou")
 elif escolha == "papel" and jogador == 0:
    print(f"Computador jogou {escolha.upper()}")
    print(f"Jogador jogou PEDRA")
    print("Computador ganhou")
 elif escolha == "papel" and jogador == 2:
    print(f"Computador jogou {escolha.upper()}")
    print(f"Jogador jogou TESOURA")
    print("Jogador ganhou")
 elif escolha == "tesoura" and jogador == 0:
    print(f"Computador jogou {escolha.upper()}")
    print(f"Jogador jogou PEDRA")
    print("jogador ganhou")
 elif escolha == "tesoura" and jogador == 1:
    print(f"Computador jogou {escolha.upper()}")
    print(f"Jogador jogou PAPEL")
    print("Computador ganhou")
 else:
  print("jogada invalida")
 print("=-"*20)

except:
    print("ERRO!!!")


