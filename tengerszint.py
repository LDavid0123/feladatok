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