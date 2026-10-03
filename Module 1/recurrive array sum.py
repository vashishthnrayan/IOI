def ArrayTotalSum(a):
    lenght = len(a)


    if lenght == 1:
        return a[0]


    return a[0] + ArrayTotalSum(a[1:])

a = [  1 ,2 ,3,6  ]
print ("ArrayTotalSum of "+"is ",ArrayTotalSum(a))