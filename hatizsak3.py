from hatizsak_alap import Hatizsák

class Hatizsak:
    def __init__(self, nev, marka, eredet, meret):
        self.nev = nev
        self.marka = marka
        self.eredet = eredet
        self.meret = meret
    def nemzet(self):
        if self.eredet == 'n':
            return 'Kiváló'
        else:
            return 'Átlagos'

tarolas=[]
for _ in range(3):
    nev=input('Add meg a neved: ')
    marka=input('Márka: ')
    eredet=input('Eredet: (Német = n) ')
    meret=int(input('Méret: '))
    t = Hatizsak(nev, marka, eredet, meret)
    tarolas.append(t)
for t in tarolas:
    print(f'{t.nev} nevű  {t.marka} márkájú {t.eredet} eredetű {t.meret} méretű hátizsák')
