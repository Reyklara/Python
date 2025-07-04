c = int(0)
n1 = 0
n2 = 0
n3 = 0
n4 = 0

while (c <= 100):
    n = int(input("Digita um número "))
    

    if (n > 0 and n <= 25):
        n1 = n1 + 1

    if (n >= 26 and n <= 50):
        n2 = n2 + 1

    if (n >= 51 and n <= 75):
        n3 = n3 + 1

    if (n >= 76 and n <= 100):
        n4 = n4 + 1
  
    p = str(input("Você deseja continuar ? "))
    if (p == "sim"):
        print("seguir digitando")
    if(p == "nao"):
        break

    c = c + 1

print(f"{n1} números estão entre [0 - 25]")
print(f"{n2} números estão entre [26 - 50]")
print(f"{n3} números estão entre [51 - 75]")
print(f"{n4} números estão entre [76 - 100]")