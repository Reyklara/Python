c = int(0)
nome_homem_velho = 0
nome_mulher_jovem = 0
idade_maior = 0
idade_menor = float('inf')

while (c < 5):
    c = c + 1
    nome = str(input("Seu Nome "))
    sexo = str(input("Seu Sexo "))
    idade = int(input("Sua Idade "))

    if (idade > idade_maior and sexo == "m" ):
        nome_homem_velho = nome
        idade_maior = idade

    if (idade < idade_menor and sexo == "f" ):
        nome_mulher_jovem = nome
        idade_menor = idade

print(f"o nome do Homem mais velho é {nome_homem_velho} e o nome mulher mais jovem é {nome_mulher_jovem}")

    