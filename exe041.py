vendas = float(input("Vendas mo Mês "))

if (vendas >= 22000):
    ano = int(input("Ano em que entrou na empresa "))
    if (ano == 2023):
        comissao = vendas * 0.03
        print("Sua comissão é de " +str(comissao))
    if (ano <= 2022):
        comissao = vendas * 0.04
        print("Sua comissão é de " +str(comissao))
    if(ano >=2024):
        comissao = vendas = 0.02
        print("Sua comissão é de " +str(comissao))