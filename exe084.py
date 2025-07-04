c = int(0)
nome = str("")
valor = float(0.0)
padraoA = (0)
padraoB = (0)
padraoC = (0)

for c in range (0,4,1):
    nome = str(input("Seu Nome "))
    valor = float(input("Valor da compra "))

    if (valor > 1000):
        padraoA = padraoA + 1

    if (valor > 500 and valor < 999.99):
        padraoB = padraoB + 1

    if (valor < 499):
        padraoC = padraoC + 1

print(f"{padraoA} são Padrão A")
print(f"{padraoB} são Padrão B")
print(f"{padraoC} são Padrão C")

