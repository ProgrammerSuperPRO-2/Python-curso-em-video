from random import randint
from random import choice
def sorteio():
    sorteios = int(input("Quantidade de números da mega-sena você deseja sortear : "))
    lista_sorteio = []
    contador = 0
    números_sorteios = 0
    lista_da_sorte = []
    lista_sorte = []
    so = []
    for c in range(0, sorteios):
        contador = contador + 1
        for c in range(0, 6):
            números_sorteios = randint(0, 60)
            lista_sorteio.append(números_sorteios)
        lista_da_sorte = lista_sorteio[:]
        lista_sorte.append(lista_da_sorte)
        print(f"Jogo {contador} : ", lista_sorteio)
        lista_sorteio.clear()

    print("A lista da sorte é : ",choice(lista_sorte))

if __name__ == "__main__":
    sorteio()