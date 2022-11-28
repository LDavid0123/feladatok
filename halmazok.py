reggeli = {'tea', 'vaj', 'piritós'}
ebed = set()
ebed = set(['halászlé', 'kenyér', True])
print(ebed)
print(reggeli)

wr = open('H:\uj\reggeli.txt','w')
wr.write('reggeli')
wr.close()

reggeli.add('lekvár')
reggeli.pop()
reggeli.remove('sajt')
reggeli.discard('sajt')
  
reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}

print(reggeli & ebed)
print(reggeli | ebed)
print(reggeli - ebed)
print(reggeli ^ ebed)

wr = open('H:\uj\ebed.txt','w')
wr.write('ebed')
wr.close()