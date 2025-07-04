c = int(0)

n = int(0)

for c in range (0,3,1):
    n = int(input("Digite um número "))

    if (n == 20):
        print("Bingo")
        break
    else:
        print("Tente novamente")