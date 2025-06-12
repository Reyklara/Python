n1 = int(input("Digita um número "))
n2 = int(input("Digita outo número "))

oper = str(input("Você quer saber a soma ou a média? "))

soma = n1 + n2
media = (n1 + n2) / 2

if(oper == "soma"):
    print(str(n1) + "+" + str(n2) + "=" + str(soma))
if(oper == "media"):
    print(str(n1) + "+" + str(n2) + "=" + str(media))
