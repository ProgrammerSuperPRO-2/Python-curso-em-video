#para esse exercício, farei utilização da pasta pasta_modulos/modulo110


from pasta_modulos import modulo110
#Esse projeto importa o modulo. Como qualquer função sem if __name__ == '__main__', ele tende a rodar o código inteiro.
modulo110.pedir_valor()
print("--"*20)
print("            RESUMO DO VALOR")
print("--"*20)
modulo110.dobro()
modulo110.metade()
modulo110.porcentagem_max(10)
modulo110.porcentagem_min(10)
print("--"*20)