def compare(n1 ,n2):
    return str(n1) + str(n2) > str(n2) + str(n1)

def largestNum3(nums):
    for i in range(len(nums), 0 , -1):
        temp = 0 
        for j in range( i ):

            if not compare(nums[j], nums[temp]):
                temp = j 
        nums[temp], nums[i- 1 ] = nums[i - 1], nums[temp]
    return str(int(''.join(map(str, nums))))


arr = [3, 30, 34, 5, 9]
print("Given Array :", arr)
print("Largest Number :", largestNum3(arr))