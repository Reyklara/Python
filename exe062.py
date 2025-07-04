brasileiro = 70
c = int(0)
maispeso = 0
menospeso = 0

while (c <= 4):
  c = c + 1
  peso = float(input("Seu Peso "))
  if (peso > brasileiro):
     maispeso = maispeso+ 1
  else:
     menospeso = menospeso + 1

print(f"existe {maispeso} pessoas que estão acima do peso médio e existe {menospeso} pessoas com peso igual ou abaixo a média")

