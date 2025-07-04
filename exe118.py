import exe118funcoes

combust = str(input("Qual combustivel deseja: \n [A]Álcool \n [Ga]Gasolina -> "))





if (combust == "A"):
    litrosA = float(input("Quantos litros você quer abastecer? "))
    exe118funcoes.abastecer(litrosA)

if (combust == "Ga"):
    litrosGa = float(input("Quantos litros você quer abastecer? "))
    exe118funcoes.abastecer2(litrosGa)
    


    




