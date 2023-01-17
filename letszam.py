szam = int(input('Adj meg az egyik iskolai számot! '))
szam2 = int(input('Adj meg az másik iskolai számot! '))
if szam > szam2:
    print('A létszám érték az egyik iskolában több')
elif szam2 > szam:
    print('A létszám érték a másik iskolában több')
else:
    print('A két szám egyenlő')