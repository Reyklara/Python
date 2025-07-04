n1 = int(input("Digita numero 1 "))
n2 = int(input("Digita numero 2 "))
n3 = int(input("Digita numero 3 "))

if (n1 > n2 and n1 > n3 and n2 > n3):
    maior = n1
    meio = n2 
    menor = n3 

if (n1 > n2 and n1 > n3 and n3 > n2):
    maior = n1
    meio = n3 
    menor = n2

if (n2 > n1 and n2 > n3 and n3 > n1):
    maior = n2
    meio = n1 
    menor = n3 

if (n2 > n1 and n2 > n3 and n3 > n1):
    maior = n2
    meio = n3 
    menor = n1 

if (n3 > n1 and n3 > n2 and n1 > n3):
    maior = n3
    meio = n1 
    menor = n2 

if (n3 > n1 and n3 > n2 and n2 > n1):
    maior = n3
    meio = n2 
    menor = n1

print("o maior é " +str(n1)+ " o do meio é " +str(n2)+ "e o menor é " +str(n3)) 