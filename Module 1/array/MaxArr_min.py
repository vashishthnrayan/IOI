def MinElement(a,size):
    temp=a[0]
    for i in range (1 ,size ):
        temp = min(temp,a[i])
    return temp

def MaxElement(a ,size):
    temp = a [0]
    for n in range (1 ,size):
        temp = max(temp,a[n])
    return temp

a = [1,2,4,67,9,34,3445,6567,1899]

size = len(a)
print("MinElemnet element of array:",MinElement)
print("MaxElement elemt of array:" , MaxElement)
print(";)")
