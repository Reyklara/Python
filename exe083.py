c = int(0)
nome = str("")
idade = int(0)
tryenome = (0)
tryeidade = (0)

for c in range (0,3,1):
    nome = str(input("Seu Nome "))
    idade = int(input("Sua Idade "))

    if (nome == "joao" and idade > 35):
        tryenome = tryenome + 1
        tryeidade = tryeidade + 1
        print("Ele é")
    else:
        print("Bloqueado")

print(f"{tryenome} nomes errados e {tryeidade} idades erradas")