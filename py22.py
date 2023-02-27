lista = []

while True:
    szo = input('"a" betűvel kezdődő szó: ')
    if not szo:
        break
    if szo[0] == 'a':
        lista.append(szo)

print('"a" betűs szavak:', lista)