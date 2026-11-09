def isPrime(A,N,X):
    i = 0


    j = N - 1

    while (i < j):

        if (A[i] + A[j] == X):
            return [A[i], A[j]]

        if (A[i] + A[j] < X):
            i += 1

        else:
            j -= 1
    return 0

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
vvl  = 17

print("Pairs with sum equal to {} is {}".format(vvl, isPrime(arr, len(arr), vvl)))