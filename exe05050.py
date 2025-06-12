n1 = int(input("Digita um numero "))
n2 = int(input("Digita um numero "))

soma = 0
subtracao = 0
multiplicacao = 0
divisao = 0

oper = str(input("Escola uma operação "))

match oper:
    case "soma":
            soma =  n1 + n2
            print(str(n1)+ "+" +str(n2)+ "=" +str(soma))
            
    case "subtração":
            subtracao =  n1 - n2
            print(str(n1)+ "-" +str(n2)+ "=" +str(subtracao))
            
    case "multiplicação":
            multiplicacao =  n1 * n2
            print(str(n1)+ "*" +str(n2)+ "=" +str(multiplicacao))
            
    case "divisão":
            divisao =  n1 / n2
            print(str(n1)+ "/" +str(n2)+ "=" +str(divisao))


    