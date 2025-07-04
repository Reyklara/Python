c = int(0)
somapar = 0
somaimpar = 0

while (c < 5):
    n = int(input("Digita um número "))
    c = c + 1
    if (c %2==0):
        somapar = somapar + n
    
    if (c %2==1):
        somaimpar = somaimpar + n


print(f"a soma dos impares é {somaimpar} e a soma dos pares é {somapar}")