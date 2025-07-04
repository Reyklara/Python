import exe122funcoes

debt = int(input("Você tem divida? \n [1]Sim \n [2]Não \n "))

if (debt == 1):
    divida = float(input("Divida da pessoa "))
    tempo = int(input("Tempo dessa divida "))
    taxa = int(input("Taxa de juros "))

    exe122funcoes.lascado(divida, tempo, taxa) 

else:
    print("Tudo Tranquilo!")

