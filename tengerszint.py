'''Írjon programot tengerszint néven!
Kérjen be addig földrajzi hely nevét és tengerszint feletti magasságát, 
amíg üres karaktert nem üt a felhasználó!

Írjon függvényt!
a tengerszintek néven, amely alföldet,"dombságot,"középhegység" és "magashegység" különböztet meg!
200m alatt alföldet,
200m és 500m között dombságot
500m és 1500m között középhegység
1500m magashegység


# Fájl írása tenger.txt néven az amelyben az összes eredmény szerepel!

Beadandó

A program forráskódja .py kiterjesztéssel a Githubra!
A program forráskódja .txt kiterjesztéssel dkt-ra!
'''




while True:
    nev = input('Kérlek add meg egy földrajzi hely nevét! ')
    if nev !=' ':
        m = int(input('Kérlek add meg a tengerszint feletti magasságát méterben! '))
    if m <= 200:
        print('a', nev,'alföldnek számít. ')
    if m > 200 and m <= 500:
        print('a', nev,'dombságnak számít.')
    elif m > 500 and m <= 1500:
        print('a', nev,'középhegységnek számít. ')
    else:
        print('a', nev,'magashegységnek számít. ')

    wr = open('tenger.txt','w')
    wr.write(nev,m,'méter magas')
    wr.close()