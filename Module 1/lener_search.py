def linear_search(l,s,e):
    for i in range(0,s):
        if l[i] == e:
            return i
    return -1
#    0,1,2,3,4,5,6,7,8
l = [1,2,3,4,5,6,7,8,9]
s = len(l)
e = int(input("Enter the element you want to search in the list:"))


result = linear_search(l,s,e)

if result != -1:
    print(f"Element is found at a position {result}")
else:
    print("Element is not found in the list")
