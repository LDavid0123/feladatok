#1
halmaz = {'1,2,3,4,5,6,7'}
halmaz.clear
print(halmaz)

#2
halmaz2 = {'a,b,c,d,e,f'}
halmaz1 = halmaz2.copy()
print(halmaz1)

#3
v1 = {"apple", "banana", "cherry"}
v2 = {"google", "microsoft", "apple"}

z1 = v1.difference(v2)

print(z1)

#4
f1 = {"alma", "banán", "cseresznye"}
f2 = {"google", "microsoft", "apple"}

f1.difference_update(f2)

print(f1)

#5
m = {"alma", "banán", "meggy"}
n = {"1", "2", "3"}

z2 = m.intersection(n)

print(z2)

#6
x = {"uborka", "ananász", "eper"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#7
c = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "facebook"}

z3 = c.isdisjoint(b)

print(z3)

#8
s = {"a", "b", "c"}
p = {"f", "e", "d", "c", "b", "a"}

z4 = s.issubset(p)

print(z4)

#9
i = {"f", "e", "d", "c", "b", "a"}
u = {"a", "b", "c"}

z5 = i.issuperset(u)

print(z5)

#10
q = {"tök", "eper", "alma"}
w = {"google", "microsoft", "apple"}

z6 = q.symmetric_difference(w)

print(z6)

#11/1
x1 = {"egy", "kettő", "három"}
y1 = {"google", "microsoft", "apple"}

z7 = x1.union(y1)

print(z7)

#11/2
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}

x.update(y2)

print(x2)

#11/3
szamok = {"egy", "kettő", "három"}

szamok.discard("kettő")

print(szamok)