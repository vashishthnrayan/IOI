input ("Set a bit - OR turn it on. Please Enter:")
print (" 5 =",bin(5)[2:])
print(" 5 | 1 =",5 | 2 ,"binary",bin(5 | 2)[2:])


input("Zero a bit - AND turn it off . Please Enter")
print("  7 = ",bin(7)[2:])
print(" 7 & 5 = ",7 & 5,"binary",bin(7 & 5)[2:])

n = int(input("Enter  a number (try 4 or 6)"))
guess = input("Is it a power of 2? (y/n)")
input("Power of 2 - only one bit is ON . press enter ")

if n>0 and (n & (n-1)) == 0:
    print(" ",n ,"  Binary :", bin(n)[2:],"  power of 2 your guess:",guess)
else:
    print(" ",n ,"  Binary :", bin(n)[2:],"  Not a power of 2 your guess:",guess)