def lascado(debt,time,inte):

    total = int(0)

    juros  = debt * time * inte
    total  = debt + juros

    print(f"Tem que pagar {total}")