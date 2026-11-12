def IsPrimeSumWithNearest(A,N,X):
    for i in range(N):
        for j in range(N):

            if (i == j):
                continue
            if (A[i] + A[j] == X):
                return [A[i], A[j]]

            if (A[i] + A[j] > X):
                break

    return 0 

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
val = 17

result = IsPrimeSumWithNearest(arr, len(arr), val)

if result != val:
    print("No pairs found with sum equal to {}. Nearest pairs with sum less than {} is {}".format(val, val, IsPrimeSumWithNearest(arr, len(arr), val-1)))
else:
    print("Pairs with sum equal to {} is {}".format(val, result))