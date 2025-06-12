preco = float(input("Preço do Produto "))
desconto = float(input("Desconto do Produto "))
novopreco = float(preco - desconto)


print("O produto custava " + str(preco) + " mas teve um desconto de " + str(desconto) + " % por isso agora esta custando " + str(novopreco) + " reais ")