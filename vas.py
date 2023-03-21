wr=open('vas.txt','r')
wr.read('vas.txt')
lista=[]
for _ in range(10):
    id=input('Add meg a személyazonosító számodat! ')
    osszeg= []
    reszosszeg= None
    lista.append(id)
    print(lista)
    if lista[0] == 3 or 4:
        for i in range(10,0,1):
            for j in lista:
                reszosszeg=i*j
                osszeg.append(reszosszeg)
                code=sum(osszeg)%11
                print(reszosszeg)
                print(code)
    if nem == "nő":
        print('Nő vagy.')
    else:
        print('Férfi vagy.')
    ev=int(input('Add meg a születési évedet. '))
    elsob=None
wr.close()