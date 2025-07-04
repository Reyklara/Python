def cobrar (km,dias):
    dia = float(60.0)
    kmRodado = float(0.15)

    total = (dias * dia) + (km * kmRodado) 

    print(f"O valor total é {total}")

