import random 

c = int(0)
soma = 0

derrotas = 0

n = random.randint(1,9) 
print(n)

n1 = int(input("Digita um número "))

while(c != 9999):
    want =  str(input("Você quer Par ou Impar? "))
    soma = n1 + n
    if (soma %2==0 and want == "par"):
        print("Você ganhou")
        break
    elif (soma %2==0 and want == "impar" or soma %2==1 and want == "par"):
        print("Você perdeu")

    if (soma %2==1 and want == "impar"):
        print("Você ganhou")
        break
    elif (soma %2==1 and want == "par" or soma %2==0 and want == "impar"):
        print("Você perdeu")

        derrotas = derrotas + 1



print(f"O jogador tive {derrotas} derrotas")


    


    

