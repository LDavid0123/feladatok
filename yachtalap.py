class Yacht:
    def __init__(self, orszag, gyarto, sebesseg):
        self.orszag=orszag
        self.gyarto=gyarto
        self.sebesseg=sebesseg
    def nemzet(self):
        if self.orszag == 'holland':
            return 'kiváló'
        else:
            return 'átlagos'

