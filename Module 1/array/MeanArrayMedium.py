def ArryMean (arr,arr_size):
    total_sum = 0
    for i in range(0,arr_size):
        total_sum += arr[i]

    return float(total_sum/arr_size)

def arrayMedian(arr,arr_size):

    sorted ( arr)

    if arr_size % 2 != 0:
        return float[arr[int(arr_size/2)]]

    return float((arr[int((arr_size-1)/2)]+ arr [int(arr_size/2)])/2.0)
arr = [1,2,3,4,5,6,7,8,5,10]
arr_size = len(arr)

print("Mean+",ArryMean(arr,arr_size))
print("Medium" , arrayMedian(arr,arr_size))