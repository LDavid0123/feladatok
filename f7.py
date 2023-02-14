valasz1 = input('Jön ma Hanna kosarazni? (igen/nem) ')
valasz2 = input('Jön ma Henrik kosarazni? (igen/nem) ')
if valasz1 ='igen' and valasz2 ='igen':
    print('mind a ketten jönnek kosarazni')
elif valasz1 ='nem' and valasz2 ='igen' or valasz1 ='igen' and valasz2 ='nem':
    print('csak az egyikük jön kosarazni.')
else:
    print('egyikük sem jön kosarazni')