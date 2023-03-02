lista = ['egy', 'kettő', 'három', 'négy', 'öt', 'hat']
lista2 = [szo.upper() for szo in lista if len(szo) > 3]
print('Eredeti:', lista)
print('Nagybetűs:', lista2)