c = int(0)
n = int(0)

divisor = int(0)

n = int(input("Digita um número "))

while (c != n):
    
    c = c + 1

    if (n %c == 0):
        divisor += 1
if (divisor == 2):     
    print("É primo")

else:
    print("Não é primo")

    