mt2 = float(input("Qtd area para ser pintada "))
gal = float(0)
lata = 0

tinta = mt2 / 6

umlt = 80 / 18
dslt = 25 / 3.6

vrtotal1 = tinta * umlt
vltotal2 = tinta * dslt 


while(mt2 >= 0):
    if (mt2 >=54):
        lata = lata + 1
        
        mt2 = mt2 - 54
        
    if (mt2 >= 10.80):
        gal = gal + 1
        
        mt2 = mt2 - 10.80

    if (mt2 < 10.80):
        gal = gal + 1
        mt2 = 0
        break
        

print(lata)

print(gal)
print(mt2)


lt18 = lata * 80
vrgalao = gal * 25

vrtotal = lt18 + vrgalao

print(f"O valor total para a situação  é {vrtotal} ")