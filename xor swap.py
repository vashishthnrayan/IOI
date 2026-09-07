input (" XOR swap : Press Enter to continue ")
print("   beafore :  a = 5, b = 9")

a, b = 5, 9
a ^= b
b ^= a
a ^= b
print("   after  :  a = ",a,", b = ",b)

n = int(input("enter a number (try 3 or 7):"))
guess =input( " what will " + str(n) + " become after swapping with 8? : ")
a,b = n, 8
a ^= b
b ^= a
a ^= b  

input("Press Enter to see what your number became after swapping with 8")
print  (" n beacame : ", a ,", your guess was : ",guess)