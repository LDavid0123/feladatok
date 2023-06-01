fuzet1=int(input('Mennyi lap van az első oldalon'))
fuzet2=int(input('Mennyi lap van a második oldalon'))
if fuzet1 > fuzet2:
    print('elso fuzet nagyobb')
elif fuzet2 > fuzet1:
    print('masodik a nagyobb')
else:
    print('egyenlo')