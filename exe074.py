cont = int(0)
nome = str("")
tel1 = int(0)
tel2 = int(0)

for cont in range (0,3,1):
    nome = str(input("Digite seu nome "))
    tel1 = int(input("Digite seu telefone 1 "))
    tel2 = int(input("Digite seu telefone 2 "))

    print(f"Nome Cadastrado {nome} e telefones cadastrados {tel1} {tel2}")