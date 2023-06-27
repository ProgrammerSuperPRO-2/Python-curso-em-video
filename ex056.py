#Variáveis:

pessoas = 0 #Ela irá contabilizar a quantidade de vezes que o código é gerado
nome = 0 #Receberá os nomes das pessoas
idade = 0 #Receberá a idade das pessoas
soma = 0 #somar a idade de todo mundo
Mais_Velho = 0 #Recebe a idade do mais velho
Mais_novo = 900000000000000000000000000000000000000000000000000000000000000000000000000 #recebe a idade do mais novo
registros = int(input("Registros desejados : ")) #Perguntará a quantidade de vezes que o código deve ser rodado
Mais_Jovens_Mulheres = 0 #receberá a quantidade de mulheres abaixo dos 20

# Estrutura de Repetição :
for p in range(0, registros):
    #código de abertura :
    pessoas = pessoas + 1
    print(f"----- {pessoas}ª PESSOA -----")
    nome = input("nome : ")
    idade = int(input("idade : "))
    sexo = input("sexo [M/F] : ")

    #If's :
    if sexo.lower().strip() == "f":
        if idade < 20:
         Mais_Jovens_Mulheres = Mais_Jovens_Mulheres + 1

    if sexo.lower().strip() == "m" or sexo.lower().strip() == "f":
        print("Registrado")
    else:
        print("ERRO!!!")

    # operação de soma :
    soma = idade + soma
    #if's :
    if idade > Mais_Velho:
        gênero_MaisVelho = sexo
        Sênior = nome
        Mais_Velho = idade
    elif idade < Mais_novo:
        Mais_novo = idade

#saída da estrutura de repetição:

#operação da média :
média = soma/registros

#Resultados :
print(f"A média da idade do grupo é : {média}")

if gênero_MaisVelho.lower().strip() == "m":
    print(f"O homem mais velho tem {Mais_Velho} anos e se chama {Sênior.capitalize()}")

elif gênero_MaisVelho.lower().strip() == "f":
    print(f"A mulher mais velha tem {Mais_Velho} anos e se chama {Sênior.capitalize()}")

print(f"Ao todo são {Mais_Jovens_Mulheres} mulheres com menos de 20 anos")
