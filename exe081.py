c = int(0)

n = int(0)
soma = (0)
trye = int(0)

for c in range (0,9,1):
    n = int(input("Digita o valor "))
    soma = soma + n
    trye = trye + 1

    if (n == 999):
        print("Pare")

    else:
        print("Tente novamente")

print(f"Foram feitas {trye} tentativas")
