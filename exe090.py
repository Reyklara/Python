c = int(0)
n = int(0)
somaimpar = 0

while (c < 500):
    if (c %5==0 and c %2==1):
        somaimpar = somaimpar + c
        
    c = c + 1 

print(somaimpar)
