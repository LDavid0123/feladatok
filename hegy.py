hegy1 = int(input('Add meg az első hegy magasságát. '))
hegy2 = int(input('Add meg a második hegy magasságát. '))
if hegy1 > hegy2:
    print('Az első hegy a nagyobb')
elif hegy2 > hegy1:
    print('A második hegy a nagyobb')
else:
    print('Ugyanakkorák a hegyek. ')

nev1=input('Add meg az egyik hegymászó nevét. ')
nev2=input('Add meg a második hegymászó nevét. ')
nev3=input('Add meg a harmadik hegymászó nevét. ')

magassag1=int(input('Add meg hogy milyen magasra mászott', nev1))
magassag2=int(input('Add meg hogy milyen magasra mászott', nev2))
magassag3=int(input('Add meg hogy milyen magasra mászott', nev3))

print(nev1, magassag1/1000, 'km magasra mászott')
print(nev2, magassag2/1000, 'km magasra mászott')
print(nev3, magassag3/1000, 'km magasra mászott')

wr = open('hegy.txt','w')
wr.write('')
wr.close()