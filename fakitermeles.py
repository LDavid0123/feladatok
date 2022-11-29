# 1 A kitermelés 50 és 100 m3 között lehetséges naponta októberben!
# 2 A legnagyobb fakitermelés mennyiségét a tervszerint 
# 3 A legkisebb fakitermelés mennyiségét a tervszerint 
# 4 Hány alkalommal volt a fakitermelés mennyiségé 82 m3 felett?
# 5 mekkora volt a fakitermelés mennyisége októberi 20.-án?
# 6 mekkora volt a fakitermelés átlag mennyisége?
# Fájl írása fa.txt néven az amelyben az összes eredmény szerepel!

import random

okt = []
for i in range(31):
    okt = random.randint(50,100)
print(okt)

maxfa=okt[0]
for fa in okt:
    if fa > maxfa:
        maxfa=fa
print(maxfa)

minfa=okt[0]
for fa in okt:
    if fa < minfa:
        minfa=fa
print(minfa)

n=len(okt)
ker = 19
i=0
while okt[0] !=ker:
    i = i + 1
print(i)

mennyiseg = 0
for mennyiseg in okt:
    if okt >= 82:
        mennyiseg = mennyiseg + 1
print(mennyiseg, 'szer volt a fakitermelés 82 m3 felett.')

osszeg = 0
for num in okt:
    osszeg = osszeg + num
print('Ennyi volt a fakitermelés átlag mennyisége: ',osszeg/31)

with open('fa.txt','w', encoding = 'utf-8')as file:
    file.write('Eredmények: {okt}{maxfa}{minfa}{mennyiseg}{osszeg}')

wr = open('fa.txt','w')
wr.write('Eredmények: {okt}{maxfa}{minfa}{mennyiseg}{osszeg}')
wr.close()