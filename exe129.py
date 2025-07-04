import exe129funcoes

cash = float(input("Saldo em Conta "))
money = int(input("Moeda para convertir \n [1]dolares \n [2]euros \n [3]iene \n "))

if (money == 1):
    exe129funcoes.dolares(cash)

if (money == 2):
    exe129funcoes.euros(cash)

if (money == 3):
    exe129funcoes.iene(cash)


