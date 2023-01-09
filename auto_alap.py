class Híres_auto:
    def __init__(self, márka_név, henger_térfogatát, nemzetiség):
        self.név = márka_név
        self. henger_térfogat = henger_térfogat
        self.nemzetiség = nemzetiség

    def elotag(self):
        if self.nemzetiség == 'n':
            return 'német'
        else:
            return 'japán'

híres_autok = []
for _ in range (3):
    marka_név = input('Add meg a márka nevét')
    henger_térfogat = int(input('Addja meg a henger_térfogatát'))
    nemzetiség = input('Add meg a márkát gyártó nemzetiségét')
    hires_auto = Híres_auto(márka_név, henger_térfogat, nemzetiség)
    hires_autok.append(hires_auto)

for hires_auto in hires_autok:
    print(f' A {hires_auto.marka_név}, egy hires {hires_auto.elotag()}, márka {henger_térfogat}')