lista = []

while True:
    szo = input('"a" vagy "A" betűvel kezdődő szó (üres szóra leáll a beolvasás): ')
    if not szo:
        break
    if szo[0] == 'a' or szo[0] == 'A':
        lista.append(szo)

print('"a" és "A" betűs szavak:', lista)