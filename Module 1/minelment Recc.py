def MinELemnetRec(a):

    length = len(a)

    if length == 1:
        return a[0]

    return min(a[0] , MinELemnetRec(a[1:]))

a = [  1 ,2 ,3,6  ]
print ("MinELemnetRec of "+"is ",MinELemnetRec(a))