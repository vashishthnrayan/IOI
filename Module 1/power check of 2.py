input("n & (n-1) clears the rightmost set bit . Press Enter ")
print("  12 & 11 =  ",12 & 11,"binary :",bin(12 & 11)[2:])
print("  8 & 7 =  ",8 & 7)


n = int(input("enter a number (try 4 or 6):"))
guess = input( " is " + str(n) + " a power of 2? (y/n): ")

input("Power of 2 : n & (n-1 ) == 0 means only one bit is ON.Press Enter")

if n>0 and (n & (n - 1)) == 0:
    print("Yes, ", n,"binary :",bin(n)[2:], " is a power of 2")
else :
    print("No, ", n, "binary :",bin(n)[2:], " is not a power of 2")