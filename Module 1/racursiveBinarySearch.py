def binarySearch(arr,l,r,x):
    while r >= l        :
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
           return binarySearch(arr,l,mid-1,x)
        else:
           return binarySearch(arr,mid+1,r,x)
    return -1

arr = [1,2,3,4,5,6,7,8,9,10,90]
x = 10

result = binarySearch(arr,0,len(arr)-1,x)

if result != -1:
    print(f"Element is found at a position {result}")
else:
    print("Element is not found in the list")