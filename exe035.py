n1 = int(input("Digita número 1 "))
n2 = int(input("Digita número 2 "))
n3 = int(input("Digita número 3 "))


somapar = 0 
somaimpar = 0

if (n1 %2==0):
    somapar = somapar + n1
if (n2 %2==0):
    somapar = somapar + n2
if (n3 %2==0):
    somapar = somapar + n3

if (n1 %2==1):
    somaimpar = somaimpar + n1
if (n2 %2==1):
    somaimpar = somaimpar + n2
if (n3 %2==1):
    somaimpar = somaimpar + n3

print("a soma dos números pares é " + str(somapar) + " e a soma dos números impares é " + str(somaimpar))