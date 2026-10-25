def max_mid(n):
    arr = [1] * n + [-1]
    current = best = arr [0]
    for x in arr[1:]:
        if current < 0 : current = x
        else :current += x
        if current >best : best = current
    return best
print("     max_mid(3) = " , max_mid(3))
print("     max_mid(4) = " , max_mid(4))

n = int(input("enter n (try 5 or 6)"))
guess = input("what is max_mid (" + str(n)+") ?")


print("     max_front ("+str(n)+ ") =", max_mid(n),"your guess :" , guess)