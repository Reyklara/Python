nome = str(input("nome do aluno "))

nota1 = int(input("Resultado Nota 1 "))
nota2 = int(input("Resultado Nota 2 "))
nota3 = int(input("Resultado Nota 3 "))
nota4 = int(input("Resultado Nota 4 "))

media = int(nota1 + nota2 + nota3 + nota4 / 4)

print("A média desse aluno é " + str(media))

if (media >= 7):
    print("O estudante " + nome + " com a nota " + str(media) + " foi aprovado")
else:
    print("O estudante " + nome + " com a nota " + str(media) + " foi reprovado")

