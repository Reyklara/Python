import random
cors = random.randint(0,2)
c = int(0)


cash = float(input("Saldo em conta -> "))
bet = float(input("Valor para apostar -> "))
cor = str(input("Escolha uma cor -> "))


if (cor == "red" and cors == 0):
    money = cash * 2

elif (cor == "black" and cors == 1):
    money = cash * 2

elif (cor == "white" and cors == 2):
    money = cash * 14

else:
    print("Você perdeu")
    money = 0


print(f"Seu saldo atual é {money}")



