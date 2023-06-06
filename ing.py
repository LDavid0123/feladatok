wr=open('ing.txt', 'w')

ing=int(input('Kérlek adj mege gy ingméretet'))
wr.write(f'Kérlek adj mege gy ingméretet')
if ing < 40:
    print('fiatal')
    wr.write(f'fiatal')
elif ing > 40 and ing =< 44:
    print('Középkorú')
    wr.write(f'középkorú')
else:
    print('Idős')
    wr.write('Idős')

wr.close()