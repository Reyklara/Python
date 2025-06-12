prod = float(input("Digite o preço do produto "))

epoca = int(input("Em que epoca do ano a gente está? \n [1] carnaval \n [2] Férias escolares \n [3] Dia das Crianças \n [4] Black Friday \n [5] Natal "))

preco_final = 0

match epoca:
    case 1:
        if (epoca == 1):
            preco_final = prod * 1.10
            
    case 2:
        if (epoca == 2):
            preco_final = prod * 1.20
            
    case 3:
        if (epoca == 3):
            preco_final = prod * 1.05
            
    case 4:
        if (epoca == 4):
            preco_final = prod * 0.70
            
    case 5:
        if (epoca == 5):
            preco_final = prod * 0.95
            
print("O preço final nessa data é " +str(preco_final))