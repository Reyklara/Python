c = int(0)

n = int(0)



n = int(input("Qual tabuada você quer ver? "))

for c in range (0,11,1):
    total = n * c
    

    print(f"{n} X {c} = {total}")