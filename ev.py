ev= [2984,2348,2069,2204,2418,2037,2092,2495,2487,2827,2305,2650]

ev = False
if (len(ev)) == 12:
    ev = True
    print(f'ez egy év adatsora')
else:
    print(f'ez egy év adatsora')

legnagyobb = ev[0]
legkisebb= ev[0]
ossz= 0
hanyszor=0
for x in ev:
    ossz +=x
    if x > legnagyobb:
        legnagyobb = x
    elif x < legkisebb:
        legkisebb = x
    if x > 2400:
        hanyszor +=1

legkisebb=min(ev)
legnagyobb=max(ev)

print(legkisebb)
print(legnagyobb)



#legnagyobb helye
hossz = len(ev)
ker = legnagyobb
i = 0
while ev[i] !=ker:
    i +=1
print(f'A legnagyobb helye: {i+1}')

#legkisebb helye
hossz = len(ev)
ker = legkisebb
i = 0
while ev[i] !=ker:
    i +=1
print(f'A legkisebb helye: {i+1}')