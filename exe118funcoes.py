def abastecer(litrosA):
    total1 = 0
    VrAlcool = float(1.90)
    if (litrosA < 20):
        total1 = litrosA * VrAlcool
        desctotal1 = total1 * 0.03
        total1 = total1 - desctotal1
        print(f"O valor a pagar é {total1}")
    
    if (litrosA >= 20):
        total2 = litrosA * VrAlcool
        desctotal2 = total2 * 0.05
        total2 = total2 - desctotal2
        print(f"O valor a pagar é {total2}")
    

def abastecer2(litrosGa):
    VrGasolina = float(2.50)
    total3 = 0
    total3 = litrosGa * VrGasolina
    desctotal3 = total3 * 0.04
    total3 = total3 - desctotal3
    print(f"O valor a pagar é {total3}")
    
    total4 = litrosGa * VrGasolina
    desctotal4 = total4 * 0.06
    total4 = total4 - desctotal4
    print(f"O valor a pagar é {total4}")
  
    

    
