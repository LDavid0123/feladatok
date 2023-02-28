import random
lista = [random.randint(1, 3) for _ in range(10)]
print('A lista:', lista)
torlendo = int(input('Törlendő: '))
lista = [szam for szam in lista if szam != torlendo]
print('A lista', torlendo, '-es nélkül:', lista)