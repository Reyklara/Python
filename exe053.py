serie = int(input("Qual serie você viu no final de semana? \n [1]Sandman \n [2]Wandinha \n [3]Game of Thrones \n [4]Dota \n [5]Dexter " ))

match serie:
    case 1:
        (serie == 1)
        serie_vista = "Sandman"
    case 2:
        (serie == 2)
        serie_vista = "Wandinha"
    case 3:
        (serie == 3)
        serie_vista = "Game of Thrones"
    case 4:
        (serie == 4)
        serie_vista = "Dota"
    case 5:
        (serie == 5)
        serie_vista = "Dexter"
        

print("A seria escolhida foi " + str(serie_vista))
        