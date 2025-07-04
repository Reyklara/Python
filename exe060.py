cont = int(input("Até quanto você quer contar? "))

c = int(0)

while (c < cont):
    c = c + 1
    print(f"{c}--")
    if (c %3 == 0):
        print("PIN \n")

