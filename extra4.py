c = int(0)
multa = float(4.0)
excesso = 0

peso = int(input("Peso do Peixe (kg) "))

if (peso > 50):
    excesso = peso - 50
    multa = multa * excesso

print(f"O pescador deve pagar de gravamen por excesso {multa}")
