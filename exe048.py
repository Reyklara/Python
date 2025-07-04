n1 = int(input("Digita um numero "))
n2 = int(input("Digita outro numero "))

maior = 0
menor = 999

if (n1 < n2):
    menor = n1 < n2

if (n2 > n1):
    maior = n2 > n1

    print("Do menor " +str(n1) + " para o maior " +str(n2))

else:
    print("os números são iguais por isso não existe maior ou menor")