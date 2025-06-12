heroe = str(input("Indica um Heroe "))
Goku=0
Naruto = 0
Kenshin = 0

arma1 = str(input("Faz KameHameHa? "))
if (Goku == "sim"):
    Goku = Goku + 1
else:
    Naruto = Naruto + 0
    Kenshin = Kenshin + 0
    
arma2 = str(input("Faz Clones de sombras? "))
if (Naruto == "sim"):
    Naruto = Naruto + 1
else:
    Goku = Goku + 0
    Kenshin = Kenshin + 0

arma3 = str(input("Faz tecnicas de espada Samurai? "))
if (Kenshin == "sim"):
        Kenshin = Kenshin + 1
else:
    Goku = Goku + 0
    Naruto = Naruto + 0
    
arma4 = str(input("Faz teletransportação? "))
if (Goku == "sim"):
    Goku = Goku + 1
else:
    Naruto = Naruto + 0
    Kenshin = Kenshin + 0
    
arma5 = str(input("Faz transformaçoes? "))
if (Goku == "sim" or Naruto == "sim"):
    Goku = Goku + 1
    Naruto = Naruto + 1
else:
    Kenshin = Kenshin + 0

arma6 = str(input("Faz Henkidama? "))
if (Goku == "sim"):
    Goku = Goku + 1
else:
    Naruto = Naruto + 0
    Kenshin = Kenshin + 0
    
    
print("Goku tem " + str(Goku) + " pontos ")
print("Naruto tem " + str(Naruto) + " pontos ")
print("Kenshim tem " + str(Kenshin) + " pontos ")






