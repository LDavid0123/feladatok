from ingalap import Ing

class Ing:
    def __init__ (self,nev,gyarto,minoseg):
        self.nev=nev
        self.gyarto=gyarto
        self.minoseg=minoseg
    
    def minőség(self):
        if self.minoseg=='n':
            return 'Kiváló'
        else:
            return 'Rossz minőségű'

lista=[]
for _ in range(3):
    nev=input('Adja meg a nevét')
    gyarto=input('Adja meg a gyártót')
    minoseg=input('Adja meg a minőségét')
    t=Ing(nev,gyarto,minoseg)
    lista.append(t)
for t in lista:
    print(f'nev: {t.nev}, a gyártó: {t.gyarto}, a minőség: {t.minőség()}')