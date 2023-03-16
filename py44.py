import random
lista = []
for _ in range(5):
    lista.append(random.randint(1, 10))
    if lista % 2:
        lista.append(lista)