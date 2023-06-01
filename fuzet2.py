def vastag(lap)
    if lap>=40:
        return True
    else:
        return False
gyarto=None
while gyarto !="":
    gyarto=input('Add meg a gyártó nevét.')
    if gyarto:
        lap=int(input('Kérem adja meg a számot.'))
        if vastag(lap):
            print(f'{gyarto},vastag füzetet gyárt')
        else:
            print(f'{gyarto},vékony füzetet gyárt')