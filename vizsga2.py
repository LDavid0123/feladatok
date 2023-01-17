nev = input('Add meg az iskola nevét! ')
pont = int(input('Add meg a pontszámát !'))
if pont >= 1000:
    print('A' ,nev,'nevű iskola nagy létszámú iskola')
elif pont <= 1000:
    print('A',nev,'nevű iskola kis létszámú iskola')