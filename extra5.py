INSS = 0
sindicato = 0
IR = 0
salarioLiquido = 0

hora = 0
vrhora = 0

vrhora = float(input("Quanto ganha por hora? "))
hora = int(input("Quantas horas trabalhou por mês? "))

salarioLiquido = vrhora * hora


IR = salarioLiquido * 0.11
INSS = salarioLiquido * 0.058
sindicato = salarioLiquido * 0.05

print(f"O salário liquido é {salarioLiquido} e o descontos de INSS é {INSS} Imposto de Renda é {IR} e Sindicato é {sindicato}")











