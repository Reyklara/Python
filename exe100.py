v = [0,0,0,0]
somapar = 0
contapar = 0
contaimpar = 0
c = int(0)

for c in range(4):
    v[c] = int(input("Valor "))

    if (v[c]%2==0):
        somapar = somapar + v[c]
    

    
        

print(f"A soma dos pares é {somapar}")

print(f"segue abaixo o vetor impar ")

for c in range(4):
    if (v[c]%2==1):
        print(v[c])


