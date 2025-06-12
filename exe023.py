buy1 = float(input("Valor Compra 1 "))
buy2 = float(input("Valor Compra 2 "))
buy3 = float(input("Valor Compra 3 "))

soma_compras = buy1 + buy2 + buy3
print(soma_compras)
media = (buy1 + buy2 + buy3) / 3
print(media)

if (soma_compras > media * 2):
    print("Verdadeiro")
else:
    print("Falso")


