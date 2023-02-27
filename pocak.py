szam = int(input('Adj meg egy páros számot! '))

for i in range(1, szam // 2 + 1):
    print('O' * i)

for i in range(szam // 2, 0, -1):
    print('O' * i)


2.

for i in range(5):
    for j in range(5):
        print('O' if i == j else '.', end = '')
    print()

3.

for i in range(7):
    for j in range(7):
        print('O' if i == j or i == 6 - j else '.', end = '')
    print()