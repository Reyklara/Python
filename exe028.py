vel = int(input("Velocidade (kms)" ))

multa = 450 + 10 * vel

if (vel <= 80):
    print("Velocidade seguro")
else:
    print("Limite de velocidade excedido. Sua multa é " + str(multa) + " reais. ")
