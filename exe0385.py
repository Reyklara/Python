
valor = float(input("Valor da hora/Aula "))
naulas = int(input("Numero de Aulas/Mês "))
salario = float(valor*naulas)
if (salario <= 1518.00):
    salario = salario - (salario * 0.075)
    print("Valor a pagar é " + str(salario))

if (salario >= 1518.00 and salario<= 2793.88):
    salario = salario - (salario * 0.09) - 22.77
    print("Valor a pagar é " + str(salario))

if (salario >= 2793.89 and salario<= 4190.83):
    salario = salario - (salario * 0.12) - 106.59
    print("Valor a pagar é " + str(salario))

if (salario >= 4190.84 and salario<= 8157.41):
    salario = salario - (salario * 0.14) - 190.40
    print("Valor a pagar é " + str(salario))




