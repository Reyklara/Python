n1 = int(input("Valor 1 "))
n2 = int(input("Valor 2 "))
n3 = int(input("Valor 3 "))

contapar = 0
contaimpar = 0

if (n1 %2==0):
    contapar = contapar + 1
if (n2 %2==0):
    contapar = contapar + 1
if (n3 %2==0):
    contapar = contapar + 1
if (n1 %2==1):
    contaimpar = contaimpar + 1
if (n2 %2==1):
    contaimpar = contaimpar + 1
if (n3 %2==1):
    contaimpar = contaimpar + 1

print("Foram encontrados " + str(contapar) + " números pares e " + str(contaimpar) + " números impares ")