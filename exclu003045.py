n1 = int(input("Digita número 1"))
n2 = int(input("Digita número 2"))
n3 = int(input("Digita número 3"))

soma1 = n2 + n3
soma2 = n1 + n3
soma3 = n1 + n2

if (n1 == soma1 and n2 == soma2 and n3 == soma3):
    print("É triangulo equilatero")
    
if (n1 < soma1 and n2 < soma2 and n3 < soma3):
    print("É triangulo escaleno")
    
if (n1 == soma1 and n2 < soma2 and n3 < soma3):
    print("É triangulo equilatero")
