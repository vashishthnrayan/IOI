def win_sum(n):
    arr = [0] * n  + [1]*n
    size = len(arr)
    for i in range (size - n + 1):
        curr_sum  = 0 
        for j in range (i , i+ n):
            curr_sum += arr[j]

        if curr_sum  == n:
            return i 
    return -1
n = int(input("what is n (try 5 or 6)"))
guess = input("what is win_sum ("+ str(n) + ")")


print(f"eqval{str(n)}) = {win_sum(n)} your guess {guess}")