def aVista(valor):
    
        total1 = valor * 0.9

        print(f"O valor da venda é {total1}")

def apPrazo(valor):

        total2 = valor * 1.1

        print(f"O valor da venda é {total2}")

def cartaoCredito(valor):

        total = valor * 1.1
        parc = 0
        parc = int(input("Quantas vezes você quer parcelar? "))
        total3 = total / parc

        print(f"O valor da venda é {total} e o numero de parcelas é {parc} o valor total é {total3}")
