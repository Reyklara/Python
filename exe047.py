km = int(input("Distância da Corrida "))

if (km <= 200):
    cobro = km * 0.35
elif(km > 200):
    cobro = km * 0.20
    perigoso = str(input("O bairro de destino é perigoso? "))
    if (perigoso == "sim" and km <= 200 ):
        cobro = km * 2
    elif (perigoso == "sim" and km > 200):
        cobro = km * 1.8
    else:
        ("Valor normal")

print("o valor final da corrida para o destino escolhido é " + str(cobro) + " reais.")



