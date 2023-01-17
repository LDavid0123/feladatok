class HíresEgyetem:
    def __init__(self, egyetemnév, város, nemzetiseg):
            self.név = egyetemnév
            self.város = város
            self.nemzetiseg = nemzetiseg
    def elotag(self):
        if self.nemzetiség == 'a':
            return 'University'
        elif nemzetiség == 'n':
            return 'Universität'

egyetem = []
for _ in range(3):
    név=input('Add meg az egyetem nevét! ')
    város=input('Add meg az egyetem városát! ')
    nemzetiseg=input('Add meg az egyetem nemzetiségét (a/n)')
    egyt = HíresEgyetem(egyetemnév, város, nemzetiség)
    egyetem.append(egyt)
for egyetemek in egyetem:
    print(egyetemek.név,egyetemek.város,egyetemek.nemzetiseg)