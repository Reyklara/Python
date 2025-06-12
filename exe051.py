terra = float(input("Digite seu Peso (Terra) "))

planeta = int(input("Escolha um planeta \n [1]Mercurio \n [2]Venus \n [3]Marte \n [4] jupiter \n [5]Saturno \n [6]Urano "))

mercurio = 0
venus = 0
marte = 0
jupiter = 0
saturno = 0
urano = 0
final = 0

match planeta:
    case 1:
            mercurio = terra * 0.37
            print("se você estivesse no planeta Mercurio você pesaria " +str(terra))
    case 2:
            venus = terra * 0.88
            print("se você estivesse no planeta Venus você pesaria " +str(terra))
    case 3:
            marte = terra * 0.38
            print("se você estivesse no planeta Marte você pesaria " +str(terra))

    case 4:
            jupiter = terra * 2.64
            print("se você estivesse no planeta Jupiter você pesaria " +str(terra))
    
    case 5:
            saturno = terra * 1.15
            print("se você estivesse no planeta Saturno você pesaria " +str(terra))
         
            
    case 6:
            urano = terra * 1.17
            print("se você estivesse no planeta Urano você pesaria " +str(terra))
          
            

            
        

