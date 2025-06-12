n1 = int(input("Digita numeor 1 "))
n2 = int(input("Digita numeor 2 "))

soma = 0
subtracao = 0
multiplicacao = 0
divisao = 0

oper = int(input("qual operação você quer fazer ")) 

soma = int(input(" [1] Soma"))
subtracao = int(input(" [2] Subtração"))
multiplicacao = int(input(" [3] Multiplicação"))
divisao = int(input(" [4] Divisão"))

if (oper == 1):
        totalsoma = soma + 1
        print(str(n1) + "+" +str(n2)+ "=" +str(totalsoma))
    
if (oper == 2):
        subtracao = subtracao - 1
        print(str(n1) - "-" +str(n2)+ "=" +str(subtracao))
    
if (oper == 3):
        multiplicacao = multiplicacao * 1
        print(str(n1) * "*" +str(n2)+ "=" +str(multiplicacao))
        
if (oper == 4):
        divisao = divisao / 1
        print(str(n1) / "/" +str(n2)+ "=" +str(divisao))
        
       