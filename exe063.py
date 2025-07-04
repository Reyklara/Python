c = int(0)
n3 = 0
n5 = 0

while (c < 7):
    n = int(input("Anota números "))
    c = c + 1
    if(c %3==0):
        n3 = n3 + n
    if(c %5==0):
        n5 = n5 + n

print(f"Foram identificados {n5} números que são múltiplos de cinco e {n3} números que são multiplo por 3.")
