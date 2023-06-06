def ing(meret):
    if meret <= 40:
        return('fiatal')
    elif meret > 40 and meret < 44:
        return('Középkorú')
    else:
        return('Idős')
    
nev=None

while nev !="":
        nev=input('Adja meg a nevét')
        if nev:
            meret=int(input('Adja meg a méretét'))
            if ing(meret):
                print(nev,ing(meret))
            else:
                print(nev,ing(meret))
        else:
            break