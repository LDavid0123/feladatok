from yachtalap import Yacht

lista=[]
for _ in range(3):
    gyarto=input('Add meg a gyártót')
    sebesseg=int(input('Add meg a sebességét'))
    orszag=input('Add meg az orszagot')
    t=Yacht(gyarto, sebesseg, orszag)
    lista.append(t)
for t in lista:
    print(f'{t.gyarto} gyártja a {t.sebesseg} sebességű {t.orszag}-ból {t.nemzet()}')