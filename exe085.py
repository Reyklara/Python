c = int(0)
n = float(0)
n1 = float(0)
n2 = float(0)
n10 = float(0)
n20 = float(0)
n50 = float(0)

n = float(input("Valor do saque R$ "))

while (c < 999):
    
    c = c + 1

    if (n >= 50):
        n50 = n50 +1
        n = n - 50

    elif (n >= 20):
        n20 = n20 +1
        n = n - 20

    elif (n >= 10):
        n10 = n10 +1
        n = n - 10

    elif (n >= 2):
        n2 = n2 + 1
        n = n - 2

    elif (n >= 1):
        n1 = n1 +1
        n = n - 1

    if (n ==0):
        break


print(f"{n50} nota(s) de R$50; {n20} nota(s) de R$20; {n10} nota(s) de R$10; {n2} nota(s) de R$2; {n1} nota(s) de R$1 para un total de R$ 185")

    
