input("power of 4 : n % 3 == 1  &   power of 8 n % 7 == 1. Press Enter  ")
print("     16  binary :",bin(16)[2:],"  16 % 3 = ",16 % 3,"  16 % 7 = ",16 % 7)
print("     8   binary :",bin(8)[2:],"  8 % 3 = ",8 % 3,"  8 % 7 = ",8 % 7)


n = int(input("enter a number (try 64 or 32):"))
guess = input( " is " + str(n) + " a power of 4? (y/n): ")

input(" n % 3 == 1 to check the power of 4. Processing..............")

pow4 = n > 0 and (n & (n - 1)) == 0 and  n % 3 == 1
if pow4:
    print("Done ! ")
    print("Yes, ", n,"binary :",bin(n)[2:], " is a power of 4",guess)
else :
    print("No, ", n, "binary :",bin(n)[2:], " is not a power of 4",guess)