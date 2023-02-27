import random
lista = [szam for szam in [random.randint(0, 50) for _ in range(10)] if not szam % 4]
print(len(lista), 'darab 4-gyel osztható jött össze:', lista)