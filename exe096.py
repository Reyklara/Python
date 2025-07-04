numero = [3,6,12,24,48,96,192,384,768,1536]

for k in numero:

    if (k == 3 or k == 6 or k == 96):
        print(f"${k}$")
    else:
        print(k)

print("------------------------------")

numeros = [3,0,0,0,0,0,0,0,0,0,0,0,0]
cont = int(0)
for cont in range(10):
    numeros[cont+1]= numeros[cont]*2
    if (numeros[cont]==3 or numeros[cont]==6 or numeros[cont]==96):
        print(f"${numeros[cont]}")
    else:
        print(numeros[cont])


