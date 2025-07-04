c = int(0)
impar = 0

while (c != 5):
       n = int(input(" Digite um número "))

       if (n %2==1 and n >= 100 and n <=200):
           print("É impar")
           impar = impar + 1

       c = c + 1

print(f"Foram encontrados {impar} entre 100 e 200")

    
