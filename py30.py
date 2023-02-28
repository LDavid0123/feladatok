jel = {'.': 'kijelentő', '?': 'kérdő', '!': 'felkiáltó / felszólító / óhatjtó'}
while True:
    mondat = input('Mondat: ')
    if not mondat:
        break
print(jel[mondat[-1]] if mondat[-1] in jel else 'ismeretlen')