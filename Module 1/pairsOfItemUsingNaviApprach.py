def IsPrimeSum(A,N,X):
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

print("Pairs with sum equal to {} is {}".format(val, IsPrimeSum(arr, len(arr), val)))