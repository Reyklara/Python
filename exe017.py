
valores = []
contador_acima_25 = 0

for i in range(3):
    valor = float(input(f"Por favor, digite o {i+1}º valor: "))
    valores.append(valor)

    if valor > 25:
        contador_acima_25 += 1 

print(f"Encontramos {contador_acima_25} número(s) maior do que 25")