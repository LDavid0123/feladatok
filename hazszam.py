def elotag(hazszam):
    if hazszam%2==0:
        return True
    else:
        return False
hazszam=None
while hazszam !='':
    hazszam=int(input('Kérem adja meg a házszámát! '))
    utca=input('Kérem adja meg az utca nevét!')
    if eldont(hazszam):
        print(f'A ház a{utca}-ban páros oldalon van')
    else:  
        print(f'a ház a{utca}-ban páratlan oldalon van')