import random
cors = random.randint(0,15)
c = int(0)
print(cors)


cash = float(input("Saldo em conta -> "))
bet = float(input("Valor para apostar -> "))
cor = str(input("Escolha uma cor -> "))


if (cor == "red" and cors >=0 and cors <= 6):
    money = cash * 2

elif (cor == "black" and cors >=7 and cors <=13):
    money = cash * 2

elif (cor == "white" and cors == 14):
    money = cash * 14

else:
    print("Você perdeu")
    money = 0


print(f"Seu saldo atual é {money}")