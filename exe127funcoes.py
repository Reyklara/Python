
def analisar(cargo):
    renda = int(0)
    if (cargo == "policial" or cargo == "medico"):
        renda  = 2000 * 12
    elif (cargo == "magico" or cargo == "coach"):
        renda = 1500 * 12
    else:
        renda = 500 * 12

    return renda
