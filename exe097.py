notas = [0.0,0.0,0.0,0.0,0.0,0.0]
media = 0
menor = 999
maior = 0
soma = 0
c = int(0)

for c in range(0,6,1):
    notas[c] = float(input("Notas "))
    soma = soma + notas[c]
    media =  soma / 6
    

    if (notas[c] > maior):
        maior = notas[c]

    elif (notas[c] < menor):
        menor = notas[c]

print(f"A Média das notas é {media}")
print(f"A Maior nota é {maior}")
print(f"A Menor nota é {menor}")
      
