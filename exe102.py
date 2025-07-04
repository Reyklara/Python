import random
v = [0,0,0,0]

c = int(0)

for c in range(4):
    v[c] = random.randint(10,20) 

soma = 0
somav = 0
soman = 0
resposta = [0,0,0,0]

print(v) 

for cont in range(4):
    resposta[cont] = int(input("digita um número "))
    
    if (v[cont] == resposta[cont]):
        
        soma  = soma + v[cont]

print(f"A soma é {soma}")