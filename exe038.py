vrcasa = float(input("Valor da Casa "))
salario = float(input("Seu Salário "))
meses = int(input("Meses a Pagar "))

prestaçao = vrcasa / meses
disponivel = salario * 0.30

if (disponivel >= prestaçao):
    print("Tem casa")
else:
    print("Não consegue")
