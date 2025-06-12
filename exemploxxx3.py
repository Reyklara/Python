import random

minha_lista = ["ouro", "prata", "bronze"]
# Escolhe 5 itens, com repetição
itens_escolhidos = random.choices(minha_lista, k=5)
print(itens_escolhidos)

# Escolhe 5 itens com pesos (ouro tem mais chance)
itens_com_peso = random.choices(minha_lista, weights=[0.6, 0.3, 0.1], k=5)
print(itens_com_peso)