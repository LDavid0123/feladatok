nevsor = []

while True:
    nev = input('Keresztnév: ')
    if not nev:
        break
    nevsor.append(nev)
    if len(nevsor) == 3:
        print('Nincs lehetőség újabb adat bevitelére')
        break

print('A névsor:', nevsor)