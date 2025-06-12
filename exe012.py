nota1 = int(input("Resultado Nota 1 "))
nota2 = int(input("Resultado Nota 2 "))
nota3 = int(input("Resultado Nota 3 "))

media = int(nota1 + nota2 + nota3 / 3)

print("A média desse aluno é " + str(media))

nota4 = int(input("Resultado Nota 4 "))

medianova = int(media + nota4 / 2)

print("A nova média será " + str(medianova))