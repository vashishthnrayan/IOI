import array as arr

a = arr.array('i')

a.append(1)
a.append(2)
a.append(4)

a.insert(2,68)

b = []
b.append(3)

for c in a :
    print(c)

for d in b:
    print(b)
    