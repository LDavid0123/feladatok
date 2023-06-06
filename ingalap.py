class Ing:
    def __init__ (self,nev,gyarto,minoseg):
        self.nev=nev
        self.gyarto=gyarto
        self.minoseg=minoseg
    
    def minoseg(self):
        if self.minoseg=='n':
            return 'Kiváló'
        else:
            return 'Rossz minőségű'
