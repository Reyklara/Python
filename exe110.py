import exe110funcoes

a = int(input("Digite valor 1 "))
b = int(input("Digite valor 2 "))
oper = str(input("Escolha uma operação "))

if(oper == "soma"):
    exe110funcoes.soma(a,b)
if(oper == "subtração"):
    exe110funcoes.subt(a,b)
if(oper == "multiplicação"):
    exe110funcoes.mult(a,b)
if(oper == "divisão"):
    exe110funcoes.divi(a,b)


