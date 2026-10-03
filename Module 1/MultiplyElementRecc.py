def multiplyElementRecc(a):
    if len(a) == 1:
        return a[0]


    return a[0] * multiplyElementRecc(a[1:])

a = [1,2,3,9]
print ("multiplyElementRecc of is ",multiplyElementRecc(a))