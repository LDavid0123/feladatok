paletta = ['piros', 'fehér', 'piros', 'piros', 'lila', 'fehér']
szin = input('Szín: ')
if szin in paletta:
    print('A', szin, len([arnyalat for arnyalat in paletta if arnyalat == szin]), '-szor szerepel a listában:', end = ' ')
else:
    print('A megadott szín nem szerepel a listában:', end = ' ')
paletta.append(szin)
print(', '.join(paletta))