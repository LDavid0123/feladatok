class balaton:
    def __init__(self, település, fekvés, nepesseg):
        self.település = település
        self.fekvés = fekvés
        self.lakszam = lakszam
    def elotag(self):
        if self.lakszam == 'é':
            return 'északi'
        elif lakszam == 'd':
            return 'déli'
    def utotag(self):
        if self.lakszam < 5000:
            return 'falu'
        elif self.lakszam < 5000 and self.lakszam > 10000:
            return 'nagyközség'
        else:
            return 'város'

telepulesek = []
for _ in range(3):
    nev=input('Add meg egy település nevét! ')
    fekves=input('Add meg a fekvését! (északi vagy déli)! ')
    lakszám=int(input('Add meg a lakosság számát (o/n)'))
    varos = balaton(település, fekvés)
    telepulesek.append(varos)

for varos in telepulesek:
    print(f'{varos.település} egy {varos.fekvés} parti város {varos.lakszam} fő lakossal. ')