v = [0,0,0,0]
c = int(0)
nine = 0

for c in range(0,4,1):
    v = int(input("Valor "))

    if (v == 9):
        nine = nine + 1
        

print(f"O número 9 apareceu {nine} vez(es)")
