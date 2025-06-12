divida = float(input("Valor da sua divida "))
tempo = int(input("Tempo da divida "))
taxa = float(input("Taxa de juros da divida "))

juros = float(divida * tempo * taxa)
total = float(divida + juros)

print("Os juros são " + str(juros) + " e o total será de " + str(total))