szam = int(input('Adj meg egy számot. '))
if szam % 3:
    print('Csak 3-mal osztható. ')
if szam % 4:
    print('Csak 4-el osztható. ')
elif szam % 3 and szam % 4:
    print('4-el és 3-mal is osztható. ')
elif szam !% 3 and szam !% 4:
    print('Sem 3-mal sem 4-el nem osztható. ')