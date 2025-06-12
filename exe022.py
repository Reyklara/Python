idade = int(input("Sua idade? "))
lingua = str(input("Você fala inglês? "))

if (lingua == "sim" and idade != 25):
    print("Verdadeiro")
elif (idade > 25 and lingua == "sim"):
    print("Verdadeiro")
elif (idade > 25 and lingua != "sim"):
    print("Falso")
