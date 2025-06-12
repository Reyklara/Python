idade = int(input("Sua Idade "))

if (idade == 18):
    sex = str(input("Seu Sexo "))
    if (sex == "masculino"):
        pais = str(input("nacionalidade "))
        if (pais == "brasileiro"):
            print("Bem-vido Soldado")
        else:
            print("Dispensado")
    else:
        print("dispensado")
else:
    print("dispensado")