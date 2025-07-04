import exe123funcoes

valor = float(input("Valor da venda "))
pag = int(input("Forma de Pagamento \n [1]a vista \n [2]a prazo \n [3]cartão de credito"))

if(pag == 1):
    exe123funcoes.aVista(valor)
if(pag==2):
    exe123funcoes.apPrazo(valor)
if(pag==3):
    exe123funcoes.cartaoCredito(valor)



