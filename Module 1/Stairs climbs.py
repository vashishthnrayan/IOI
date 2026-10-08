def ways(stairs):
    if stairs < 0:
        return 0
    elif stairs == 0:
        return 1
    else:
        return ways(stairs - 1) + ways(stairs - 2)

input ("ways counts every distinct path up n stairs -1 steps or 2 steps at a time . Press enter")

print("ways(3)=",ways(3))
print("ways(4)=",ways(4))


n = int(input("Enter the number of stairs to climb: "))
guess  = input ("what is way " + str(n) + "?")
input ("ways counts every distinct path up n stairs -1 steps or 2 steps at a time . Press enter")
print("ways(",str(n),")=",ways(n),"your guess was",guess)