c = int(0)
francisco = float(1.50)
sara = float(1.10)
anos = 0

for c in range (0,200,1):
    francisco = francisco + 0.02
    sara = sara + 0.03

    if (sara > francisco):
        break

print(f"Foram necesarioas {c}")

