c = int(0)
mediapos = 0
contapos = 0
contaneg = 0
soma = int(0)

while (c != 9999):
    c = c + 1
    n = int(input("Digita um numero "))
    r = str(input("Você quer continuar? "))

    if (n > 0):
        soma = soma + n
        contapos = contapos + 1
        mediapos = soma / contapos

    if (n < 0):
        contaneg = contaneg + 1


    print(f"A média dos valores positivos é {mediapos}")
    print(f"A quantidade dos valores positivos é {contapos}")
    print(f"A média dos valores negativos é {contaneg}")