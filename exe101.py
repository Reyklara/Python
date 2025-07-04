v = [0,0,0,0]
somapar = 0
contapar = 0
somaimpar = 0
contaimpar = 0

for c in range(0,4,1):
    v[c] = int(input("Valor "))

    if (v[c] %2 == 0):
        somapar = somapar + v[c]
    

    if (v[c] %2 == 1):
        print(f"{v[c]}")

print(f"A soma dos pares é {somapar}")




