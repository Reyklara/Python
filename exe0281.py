vel = int(input("Velocidade (kms)" ))

excesso = vel - 80


if (vel <= 80):
    print("Velocidade seguro")
elif(excesso >= 0 and excesso <= 20):
    multa = 150 + 5 * excesso
    print("Limite de velocidade excedido. Sua multa é " + str(multa) + " reais. ")

elif(excesso >= 21 and excesso <= 80):
    multa1 = 250 + 10 * excesso
    print("Limite de velocidade excedido. Sua multa é " + str(multa1) + " reais. ")

elif(excesso >= 81 and excesso <= 200):
    multa2 = 500 + 20 * excesso
    print("Limite de velocidade excedido. Sua multa é " + str(multa2) + " reais. ")

else:
    print("o veiculo será confiscado")



