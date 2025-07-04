c = int(0)
soma = 0
cont = 0

while ( c != 9999):
    n = int(input("Digita um número "))
    c = c + 1
    soma = soma + n
    cont = cont + 1
    

    if (n == 999):
        print("Chegou!")
        break
        
soma = soma - 999
print(f"A soma dos valores é {soma} e {cont} tentativas feitas")