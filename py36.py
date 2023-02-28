betuk = []
while True:
    betu = input('Betű: ')
    if not betu:
        break
    if betu.lower() in betuk or betu.upper() in betuk:
        print('Ezt a betűt már rögzítettem')
    else:
        betuk.append(betu)
        betuk.sort()
    print('Rögzített betűk:', betuk)