n1 = int(input("Digite o primeiro valor "))
n2 = int(input("Digite o segundo valor "))
n3 = int(input("Digite o terceiro valor "))

contador_maior_25 = 0

if n1 > 25:
    contador_maior_25 = contador_maior_25 + 1
if n2 > 25:
    contador_maior_25 = contador_maior_25 + 1
if n3 > 25:
    contador_maior_25 = contador_maior_25 + 1

print("Encontramos " + str(contador_maior_25) + " valor(es) acima do que 25")
