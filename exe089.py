c = int(0)
n = int(0)
somapar = 0
contapar = 0

for c in range (0,6,1):
    n = int(input("Digite o valor "))

    if (n %2==0):
        somapar += n
        contapar += 1

print(f"foram digitados {contapar} pares e a soma deles é {somapar}")