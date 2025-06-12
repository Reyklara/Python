nota1 = float(input("Resultado Nota 1 "))
nota2 = float(input("Resultado Nota 2 "))
frequencia = int(input("Frequência "))

media = nota1 + nota2 / 2

if (media >= 60 and frequencia > 75):
    print("Aprovado")

if (media > 40 and media < 60):
    print("Está de Recuperação")
    notarecup = float(input("Nota de Recuperação "))
    if (notarecup  <= 69.99 ):
        print("Reprovado")
    else:
        print("Aprovado")

if (media < 40):
    print("Reprovado sem direito a recuperação")

