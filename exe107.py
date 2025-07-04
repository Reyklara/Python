c = int(0)

buy = float(input("Valor da compra "))
pay = str(input("Forma de Pagamento "))

if (pay == "pix" or pay == "a vista"):
    valortotal = buy - (buy * 0.10)
    print(f"Voce tem um desconto de {valortotal} ")

if (pay == "cartão debito" ):
    valortotal = buy - (buy * 0.05)
    print(f"Voce tem um desconto de {valortotal} ")

if (pay == "cartão credito"):
    valortotal = buy + (buy * 0.05)
    parcela = int(input("Quantas parcelas? "))
    if (parcela <= 3):
        parcela1 = buy / parcela

        print(f"sua compra de {buy} parcelada em {parcela} de {parcela1} sendo um total de {valortotal} ")

if (pay == "cartão credito"):
    valortotal = buy + (buy * 0.10)
    parcela = int(input("Quantas parcelas? "))
    if (parcela > 3):
        parcela2 = buy / parcela

        print(f"sua compra de {buy} parcelada em {parcela} de {parcela2} sendo um total de {valortotal} ")
