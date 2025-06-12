excel = int(input("Seu conhecimento em Excel? \n [1]Basico \n [2]Intermediario \n [3]Avançado "))

match excel:
    case 1:
        if (excel == 1):
            formulas = int(input("Para que sirven as formulas: \n [1]SOMA \n [2]MÉDIA \n [3]MÁXIMO "))
            if (formulas == 1):
                print("Entrega o valor somado de dois ou mais valores")
            if (formulas == 2):
                print("Entrega o valor somado de dois ou mais valores, mais a divisão desses dois valores")
            if (formulas == 3):
                print("Entrega o valor maior de dois ou mais valores")
                

    case 2:
        if (excel == 2):
            formula = int(input("Para que sirven as formulas: \n [1]SE \n [2]Somase \n [3]Cont.Se "))
            if (formula == 1):
                print("Dá condicionales aos valores")
            if (formula == 2):
                print("Soma varios valores dentro de uma condicional")
            if (formula == 3):
                print("Da a quantidade dos valores dentro de uma condicional")
                
                
    case 3:
        if (excel == 2):
            formule = int(input("Para que sirven as formulas: \n [1]Ordem.eq \n [2]ProcH \n [3]ProcV "))
            if (formule == 1):
                print("Ordena os valores de um jeito equitativo")
            if (formule == 2):
                print("Dá os valores de uma fila a outra")
            if (formule == 3):
                print("DDá os valores de uma coluna a outra")