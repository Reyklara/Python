def investigar(a,b,c,d,e):
    pontos = int(0)
    if (a  == "sim"):
        pontos = pontos + 1
    if (b  == "sim"):
        pontos = pontos + 1
    if (c  == "sim"):
        pontos = pontos + 1
    if (d  == "sim"):
        pontos = pontos + 1
    if (e  == "sim"):
        pontos = pontos + 1

    if (pontos == 2):
        print("Suspeita")

    if (pontos >=3 and pontos <=4):
        print("Cumplice")

    if (pontos >= 5):
        print("Assassino")

    else:
        ("Inocente")
   