c = int(0)
nome = str("")
sexo = str("")
homens = int(0)

for c in range (0,3,1):
    nome = str(input("Seu Nome "))
    sexo = str(input("Seu Sexo "))

    if (sexo == "masculino"):
        homens = homens + 1

print(f"{homens} hombre(s) foram cadastrados")


