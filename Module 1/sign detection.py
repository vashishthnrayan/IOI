input ("XOR sign detection : Press Enter to continue ")
print(" 4 ^ 2 = ",4 ^ 2,"same sign means positive")
print(" 4 ^ -2 = ",4 ^ -2,"different sign means negative")

n = int(input("enter a number (try 3 or -7):"))
guess = input( " what will " + str(n) + " become after XOR with 8? : ")
input("XOR is negitive when signs differ .pree enter ")
print(" ",n,"^ -8 =",n ^ -8,"your guess was : ",guess)