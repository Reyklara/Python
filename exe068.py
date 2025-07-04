c = int(0)

while (c != 999999):
    user = str(input(" Usuario "))
    passw = str(input(" Senha "))

    if (user == "facil" and passw == "ff"):
        print("Acesso Correto")
        break
    else:
        print("você será multado em R$2,00 pela sua falha")
        answer = str(input("Gostaria de tentar novamente?"))
    if (answer == "não"):
        break

        

    
