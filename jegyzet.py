jegyzet = input('Adja meg a file nevét! ')
while jegyzet !='stop':
    jegyzet = input('Adja meg a file nevét! ')
    wr = open(jegyzet,'w')
    wr.write('valami')
    wr.close()
