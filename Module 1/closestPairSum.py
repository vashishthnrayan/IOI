MAX_val = 1000000 
def  PrintClosePair(arr,n,x):

    res_1,res_r= 0 ,0 

    l,r,diff = 0, n-1, MAX_val

    while r > l:
        if abs (arr[i] + arr[r] - x) < diff:
            res_l= l
            res_r= r
            diff =abs(arr[l] + arr[r] - x)
        if[arr[l] + arr[r] ] > x:
            r -= 1
        else:
            l += 1
        print("The closest pair is {} and {}".format(A[res_l], A[res_r]))


if __name__ == "__main__":
    arr = [10 , 3,690,445,235]
    n = len(arr)
    x = 1135
    PrintClosePair (arr, n, x)