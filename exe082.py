c = int(0)
idade = int(0)
sex = str("")
pessoas = (0)
mulheres = (0)
homens = (0)

for c in range (0,4,1):
    idade = int(input("Sua Idade "))
    sex = str(input("Seu Sexo "))

    if (idade > 10):
        pessoas = pessoas + 1

    if (idade < 20 and sex == "feminino"):
        mulheres = mulheres + 1

    if (sex == "masculino"):
        homens = homens + 1

print(f"{pessoas} pessoas tem mais de 10 anos")
print(f"{homens} homens foram cadastrados")
print(f"{mulheres} mulheres tem menos de 10 anos")

