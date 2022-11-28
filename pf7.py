import random

szám1 = int(input('Adj meg egy változót! '))
szám2 = random.randint(10,50)
szám3 = 86

print(szám1, szám2, szám3)


if szám1 % 2:
    print('Páratlan a szám')
else:
    print('Páros a szám')


számok = [86,700,1]
print(számok)

szam = int(input('Adj meg 5 további számot. '))
szam = számok.append(szam)
print(számok)

szam1 = 0
for num in számok:
    szam1 = szam1 + num

print('Összesen: ', számok)


halmaz1 = {86,700,1}
halmaz = set()
halmaz = set([12,45,True])
print(halmaz)
print(halmaz1)

halmaz1.add('87')
halmaz1.pop()
halmaz1.remove('700')
halmaz1.discard('700')

with open ('ld.txt','w', encoding = 'utf-8') as file:
    file.write('86,700,1')

print('86,700,1')