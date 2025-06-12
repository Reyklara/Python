idade = int(input("Qual é sua idade? "))
pais = str(input("Qual é sua nacionalidade? "))
sexo = str(input("Qual é seu sexo? "))

if(sexo == "masculino" and idade == 18 and pais == "brasileiro"):
    print("Apto")
else:
    ("Não Apto")