c = int(0)
n = int(0)
soma = (0)
somapar = (0)
somaimpar = (0)
contapar = 0
contaimpar = 0


for c in range (0,4,1):
    n = int(input("Digita um número "))
    
    soma = soma + n
    if (n %2==0):
        somapar = somapar + 1
        contapar = contapar + 1

    if (n %2==1):
        somaimpar = somaimpar + 1
        contaimpar = contaimpar + 1

        
        
    
    
    
    
    

print(f"Foram cadastrados {contapar} números pares")
print(f"Foram cadastrados {contaimpar} números impares")
print(f"A soma dos pares é {somapar}")
print(f"A soma dos impares é {somaimpar}")
print(f"A soma geral é {soma}")
