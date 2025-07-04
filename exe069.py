c = int(0)

while (c < 3):
    n = int(input("Digita um número "))
    c = c + 1

    if (n == 20):
        print("Bingo!")
        break
    else:
        if (c == 3):
            print("você perdeu")
            break