print("Covid19")

sim = 1
nao = 2
suspeito = 0
numPac = int(input("Informe a quantidade de pacientes"))
for x in range (numPac):
    tosse = int(input("Tem tosse? "))
    febre = int(input("Tem febre? "))
    resp = int(input("Tem dificultade de respirar? "))

if (tosse == 1 and febre == 1 and resp == 1):
    suspeito +=1  
    print("Voce tem Covid 19")
elif (tosse == 1 and febre == 1 and resp == 2 or tosse == 1 and febre == 2 and resp == 2):
    suspeito +=1
    print("Voce naõ tem Covid 19")
else:
    ("Você é paranoico")
    


