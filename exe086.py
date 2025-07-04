import random

c = int(0)
maior = (0)
menor = 999
trye = (0)

n = random.randint(0,10)
print(n)



while (c < 20):
    v = int(input("Digita o numero "))
    
    c = c + 1
    

    if (v < n):
        
        print("Você errou! Tente um numero maior.")

    elif (v > n):
        print("Você errou! Tente um numero menor.")

    elif (n == v):
        trye = trye + 1

        print(f"Sucesso! Você acertou após de {trye} tentativas")
        break




        







