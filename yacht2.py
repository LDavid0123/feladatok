def csomo(km):
    sebesseg=1.852*km
    return sebesseg

hnev=None
while True:
    hnev=input('add meg a yacht nevét')
    if hnev == '':
        break
    km=int(input('Add meg a yacht sebességét.'))
    if csomo(km) > 100:
        print('a hajo gyors ')
    else:
        print('a hajo atlagos gyorsasagu')