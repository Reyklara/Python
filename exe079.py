c = int(0)

nome = str("")
sex = str("")
homens = int(0)

for c in range (0,3,1):
    nome = str(input("Digite seu nome "))
    sex = str(input("Seu Sexo "))

    if (sex == "masculino"):
        homens = homens + 1

print(f"{homens} homens foram cadastrados")