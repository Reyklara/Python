c = int(0)
n = int(0)
soma = 0
excedeed = 0

for c in range (0,200,1):
    n = int(input("Digita o valor "))
    soma = soma + n
    excedeed = soma - 1000

    if (soma > 1000):
       break


print(f"Excedeu em {excedeed}")


