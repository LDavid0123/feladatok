jegyzet = input('Adja meg a file nevét! ')
while jegyzet !='stop':
    wr = open(jegyzet,'w')
    wr.write('írás')
    wr.close()