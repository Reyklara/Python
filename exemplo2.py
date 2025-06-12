a = int(input("digite um numero"))

if (a > 10):
    print("Deu certo")
else:
    ("Deu errado")

if(a > 10 and a < 20):
    print("Deu certo 1")
elif(a > 20 and a < 30): #elif equivale a senao se de portugol
    print("Deu certo 2")
else:
    print("Deu errado")

#para sorteios

import random 

a = random.randint(10,20) # ou pode ser a = int(random.randint(10,20))

print(a)