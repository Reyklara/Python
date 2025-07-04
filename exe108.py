import random
cpu = random.randint(0,2)
c = int(0)
print(cpu)

j = int(input("Qual você quer jogar ? \n [0]Pedra \n [1]Papel \n [2]Tesoura "))


if (cpu == 0 and j == 0):
    print("Empate a")
elif (cpu == 0 and j == 1):
    print(j)
    print("Você Perdeu b" )
elif (cpu == 0 and j == 2):
    print("Você perdeu c")
elif (cpu == 1 and j == 0):
    print("Você perdeu d")
elif (cpu == 1 and j == 1):
    print("Empate e")
elif (cpu == 1 and j == 2):
    print("Você ganhouf")
elif(cpu == 2 and j == 0):
    print("Você ganhou g")
elif (cpu == 2 and j == 1):
    print("Você perdeu h")
elif (cpu == 2 and j == 2):
    print("Empate i")

