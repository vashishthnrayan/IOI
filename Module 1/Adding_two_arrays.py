def add_arrays(arr1, arr2 ,index=0):
    if index  == len(arr1   ):
        return []

    curnt_sum = arr1[index] + arr2[index]

    return [curnt_sum] + add_arrays(arr1,arr2,index+1)

arr1 = [1, 2, 3,4]
arr2 = [4, 5, 6,7]

result = add_arrays(arr1, arr2)
print("Resultant array after addition:", result)