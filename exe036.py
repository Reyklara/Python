n1 = int(input("Digita número 1 "))
n2 = int(input("Digita número 2 "))
n3 = int(input("Digita número 3 "))
n4 = int(input("Digita número 4 "))

maior = 0
somapar = 0
contapar = 0
maiorpar = 0

if (n1 %2==0):
    somapar = somapar + n1
    contapar = contapar + 1
if (n2 %2==0):
    somapar = somapar + n2
    contapar = contapar + 1
if (n3 %2==0):
    somapar = somapar + n3
    contapar = contapar + 1
if (n4 %2==0):
    somapar = somapar + n4
    contapar = contapar + 1

if (n1 > maior):
    maiorpar = n1
if (n2 > maior):
    maiorpar = n2
if (n3 > maior):
    maiorpar = n3
if (n4 > maior):
    maiorpar = n4

print("Foram digitados " + str(contapar) + " números pares")
print("A soma desses números pares é " + str(somapar))
print("O maior numero par é " + str(maiorpar))