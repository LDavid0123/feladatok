import random
oszthato = [j for j in [random.randint(1, 12) for i in range(20)] if not j % 3]
print(len(oszthato), 'véletlen szám osztható 3-mal:', oszthato)