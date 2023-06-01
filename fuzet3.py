from fuzetalap import Fuzet

lista=[]
for _ in range(3):
    gyarto=input('Add meg a gyártót')
    lapszam=int(input('Add meg a lapszámot'))
    minoseg=input('Melyik orszagbol szarmazik?')
    t=Fuzet(gyarto, lapszam, minoseg)
    lista.append(t)
for t in lista:
    print(f'{t.gyarto}gyártja {t.vastag()}lapszamu {t.minoseg1()}minőségű könyvet gyártja')