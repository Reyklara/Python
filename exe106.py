import random
n = random.randint(0,10)
c = int(0)
print(n)




cash = float(input("Saldo em conta -> "))
bet = float(input("Valor para apostar -> "))
mult = float(input("Escolha um multiplicador -> "))


if (mult == 1.1 and n >=1 and n <=9):
    money = bet * 1.1

elif (mult == 1.3 and n >=1 and n <=8):
    money = bet * 1.3

elif (mult == 1.6 and n >=1 and n <=5):
    money = bet * 1.6

elif (mult == 4 and n >=1 and n <=2):
    money = bet * 2

elif (mult == 2.5 and n >=1 and n <=2):
    money = bet * 2

else:
    print("Você perdeu")
    money = 0

prim = str(input("É sua primeira vez? "))
if (prim == "sim"):
    money = bet


print(f"Seu saldo atual é {money}")
