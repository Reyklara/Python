n = [0,0,0]
c = int(0)
fourteen = 0

for c in range(0,3,1):
    n = int(input("Número "))

    if (n == 14):
        fourteen = fourteen + 1

print(f"O número 14 apareceu {fourteen} vez(es)")