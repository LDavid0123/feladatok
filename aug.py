aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]

'''Lehet e augusztus havi hóméséklet
A legnagyobb hóméséklet
A legkisebb hóméséklet
Hány alkalommal volt a hőmeséklet 31 fok felett?
mekkora volt a hómérséklet augusztus 20.-án?
mekkora volt az átlag hőmérséklet?
mekkora volt a hőingadoszás?
Fájl írás'''

with open ('H:/uj/ld.txt','w', encoding = 'utf-8') as file:
    file.write('fok')

wr = open('uj/ld.txt','w')
wr.write('fájlírás')
wr.close()


havih = 31
if havih >= 31:
    print('igen')

fok = aug[0]
for elem in aug:
    if elem > fok:
        elem = fok
print(fok, 'Celsius fok volt a legnagyobb hőmérséklet')

fok2 = aug[0]
for elem2 in aug:
    if elem < fok2:
        elem = fok2
print(fok2, 'Celsius fok volt a legkisebb hőmérséklet')


ker = 31
print(ker, 'Celsius fok volt 20.-án')


osszeg = 0
for num in aug:
    osszeg = osszeg + num
print(osszeg/31, 'Celsius fok volt az átlag havi hőmérséklet')