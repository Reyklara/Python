idade1 = int(input("Idade Pessoa 1 "))
idade2 = int(input("Idade Pessoa 2 "))


if (idade1 == 9 and  idade2 == 9):
    categoria1 = "mirim"
    hora = int(input("Horario da luta"))
    print("Esta marcada a luta na hora " + str(hora))
    

elif (idade1 >= 10 and idade1 <= 14 and  idade2 >= 10 and idade2 <= 14):
    categoria2 = "infantil"
    hora = int(input("Horario da luta"))
    print("Esta marcada a luta na hora " + str(hora))

elif (idade1 >= 15 and idade1 <= 18 and idade2 >= 15 and idade2 <= 18 ):
    categoria3 = "jovem"
    hora = int(input("Horario da luta"))
    print("Esta marcada a luta na hora " + str(hora))

elif (idade1 >= 19 and idade1 <= 24 and idade2 >= 19 and idade2 <= 24 ):
    categoria4 = "adulto"
    hora = int(input("Horario da luta"))
    print("Esta marcada a luta na hora " + str(hora))

else:
    print("Luta cancelada")


    

    
