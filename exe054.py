humor = int(input("Escolha um humorista \n [1]Fabio Porchat \n [2]Danilo Gentili \n [3]Rafinha Bastos "))


cidade = str(input("Qual é sua cidade? "))
idade = 0

match humor:
    case 1:
        if (cidade == "araxá"):
            idade = int(input("Qual é sua idade? "))
            if (idade > 18):
                print("tem show do Fabio Porchat")

                
    case 2: 
        if (cidade == "são paulo"):
            print("tem show do Danilo Gentili")
            
    case 3: 
        if (cidade == "Rio de Janeiro"):
            print("tem show do Rafinha Bastos")