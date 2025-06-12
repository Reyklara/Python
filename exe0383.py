valor = float(input("Valor do produto "))
pago = str(input("Forma de pagamento "))



if (pago == "dinheiro" or pago == "pix"):
    valor = valor -(valor*0.15)
    print("O valor a pagar é de " + str(valor))

if (pago == "cartão de credito"):
    valor = valor -(valor*0.10)
    print("O valor a pagar é de " + str(valor))

if (pago == "cartão debito"):
    parcelas = int(input("Quantas parcelas? "))
    if (parcelas <= 2):
            parcelas1 = valor / parcelas
            print("O valor será debitado em 2 parcelas " + str(parcelas1)+ " reais ")
    if (parcelas > 2):
         valor = valor * 0.10
         parcelas1 = valor / parcelas
         print("O valor será debitado em 3 parcelas de " + str(parcelas1) + " reais ")



    




