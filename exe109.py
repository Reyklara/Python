import random
cpu = random.randint(0,5)
c = int(0)
print(cpu)


j = int(input("Qual você quer jogar ? \n [0]Pedra \n [1]Papel \n [2]Tesoura \n [3]Lagarto \n [4]Spock "))


if (cpu == 0 and j == 0):
    print("Empate")
elif (cpu == 0 and j == 1):
    print("Você Perdeu" )
elif (cpu == 0 and j == 2):
    print("Você perdeu")
elif (cpu == 0 and j == 3):
    print("Você Ganhou" )
elif (cpu == 0 and j == 4):
    print("Você Perdeu" )
elif (cpu == 1 and j == 0):
    print("Você perdeu")
elif (cpu == 1 and j == 1):
    print("Empate")
elif (cpu == 1 and j == 2):
    print("Você ganhou")
elif (cpu == 1 and j == 3):
    print("Você Perdeu" )
elif (cpu == 1 and j == 4):
    print("Você Perdeu" )
elif(cpu == 2 and j == 0):
    print("Você perdeu")
elif (cpu == 2 and j == 1):
    print("Você Ganhou")
elif (cpu == 2 and j == 2):
    print("Empate")
elif (cpu == 2 and j == 3):
    print("Você Perdeu" )
elif (cpu == 2 and j == 4):
    print("Você ganhou" )
elif (cpu == 3 and j == 1):
    print("Você Ganhou" )
elif (cpu == 3 and j == 2):
    print("Você ganhou" )
elif (cpu == 3 and j == 3):
    print("Empate" )
elif (cpu == 3 and j == 4):
    print("Você Perdeu" )
elif (cpu == 4 and j == 0):
    print("Você Perdeu" )
elif (cpu == 4 and j == 2):
    print("Você Ganhou" )
elif (cpu == 4 and j == 3):
    print("Você Perdeu" )
elif (cpu == 4 and j == 4):
    print("Empate" )


print(f"O sorteio foi {cpu} e o gnhador foi {j} ")