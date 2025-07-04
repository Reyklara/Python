import exe128funcoes
import random

r = random.randint(0,10)

a = int(input("Digite valor 1 "))
b = int(input("Digite valor 2 "))
c = int(input("Digite valor 3 "))
d = int(input("Digite valor 4 "))

print(r)

c1 = exe128funcoes.analise3(c)
b1 = exe128funcoes.analise2(b)

total = (c1 + b1) * 3.14
print(f"O resultado dos dois valores é {total}")

