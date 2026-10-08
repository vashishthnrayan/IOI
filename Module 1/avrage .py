def find_sum(arr,n):
    if n == 0:
        return 0
    else:
        return  arr[n - 1] + find_sum(arr, n - 1)

arr = [10 ,20,30,40,50,60,89,26,45,95]
total =  find_sum(arr, len(arr))

avg = total / len(arr)

print ("Avg  - ",avg)
