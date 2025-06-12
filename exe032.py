id1 = int(input("Idade pessoa 1 "))
id2 = int(input("Idade pessoa 2 "))
id3 = int(input("Idade pessoa 3 "))
id4 = int(input("Idade pessoa 4 "))

maior = 0
menor = 999

if (id1 > maior):
    maior = id1
if (id2 > maior):
    maior = id2
if (id3 > maior):
    maior = id3
if (id4 > maior):
    maior = id4

if (id1 < menor):
    menor = id1
if (id2 < menor):
    menor = id2
if (id3 < menor):
    menor = id3
if (id4 < menor):
    menor = id4

print("O mais jovem tem " + str(menor) + " anos e o mais velho tem " + str(maior) + " anos")

